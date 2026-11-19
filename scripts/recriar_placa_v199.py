from pathlib import Path
from PIL import Image
from scipy.ndimage import distance_transform_edt
import numpy as np,json,hashlib
ROOT=Path(__file__).resolve().parent.parent
import argparse,zipfile
p=argparse.ArgumentParser();p.add_argument('--original',type=Path,required=True);p.add_argument('--base',type=Path);p.add_argument('--saida',type=Path,default=ROOT/'Recriado');args=p.parse_args()
OUT=args.saida;OUT.mkdir(parents=True,exist_ok=True)
for folder in ['ROMs','Patches','Capturas','Scripts','Resultados']:(OUT/folder).mkdir(exist_ok=True)
a=np.array(Image.open(ROOT/'assets/rebuild/v199/placa_indices_original.png'));pal=np.array(json.loads((ROOT/'assets/rebuild/v199/paleta_original.json').read_text()),dtype=np.uint8);mapping=np.load(ROOT/'assets/rebuild/v199/montagem_sprites.npy')
flat=np.zeros((80,64),np.uint8)
for x in range(64):
 sh=round((x-8)*.14)
 for y in range(72):
  if 0<=y+sh<80:flat[y+sh,x]=a[y,x]
ink=flat>=13
# Native hand-painted glyphs, taken exclusively from the original sign.
font={}
for ch,x0,x1,y0,y1 in [('K',9,16,13,23),('O',16,24,13,23),('N',23,30,24,34),('G',33,40,13,23),('S',43,48,13,23),('B',9,16,24,34),('A',16,23,24,34),('D',42,49,34,44)]:
 f=flat[y0:y1,x0:x1].copy();f[f<13]=0;font[ch]=f
# Original lettering has uneven strokes; keep its three ink shades and native shapes.
def word(s,width=None,height=10):
 f=flat[13:23,9:40].copy() if s=='KONG' else np.concatenate([font[c] for c in s],axis=1)
 f[f<13]=0
 if (width and f.shape[1]>width) or f.shape[0]>height:
  # BOX on alpha and shade separately prevents transparency becoming dark wood.
  alpha=np.float32(f>0);light=np.float32(np.where(f>0,f,0))
  sz=(min(width or f.shape[1],f.shape[1]),height);aa=np.array(Image.fromarray(alpha).resize(sz,Image.Resampling.BOX));ll=np.array(Image.fromarray(light).resize(sz,Image.Resampling.BOX))
  f=np.where(aa>=.42,np.clip(np.rint(ll/np.maximum(aa,.001)),13,15),0).astype(np.uint8)
 return f
# Remove only original lettering; recover each covered wood pixel from nearby wood of the same plank.
clean=flat.copy();plank_ranges=[(10,24),(24,35),(34,45)]
for y0,y1 in plank_ranges:
 region=np.zeros_like(ink);region[y0:y1,4:54]=True;to_fill=ink&region
 # Prefer candidates on the same horizontal grain line and avoid outlines/seams.
 valid=(flat>=3)&(flat<=12)&region
 sy,sx=np.where(valid)
 for y,x in zip(*np.where(to_fill)):
  score=(sx-x)**2+((sy-y)*2.8)**2
  k=np.argmin(score);clean[y,x]=flat[sy[k],sx[k]]
text=np.zeros_like(flat)
placements=[]
for s,y,width in [('BANANAS',13,43),('DO',25,None),('KONG',34,None)]:
 f=word(s,width,8 if s=='KONG' else 10);x=round(28-f.shape[1]/2);text[y:y+f.shape[0],x:x+f.shape[1]]=f;placements.append({'text':s,'x':x,'y':y,'width':f.shape[1],'height':f.shape[0]})
fixedflat=np.where(text>0,text,clean).astype(np.uint8)
fixed=a.copy();newink=np.zeros_like(a,dtype=bool)
for x in range(64):
 sh=round((x-8)*.14)
 for y in range(72):
  ny=y+sh
  if 0<=ny<80:
   fixed[y,x]=fixedflat[ny,x];newink[y,x]=text[ny,x]>0
# Text must stay on the original wooden object, including a one-pixel safety margin.
silhouette=a>0;dist=distance_transform_edt(silhouette)
outside=np.argwhere(newink&~silhouette)
print('new ink',int(newink.sum()),'outside wood',len(outside),'minimum margin',float(dist[newink].min()))
assert not len(outside),outside
assert dist[newink].min()>=1.0
# Restore all source tiles first: this removes remnants of the old translation outside the planks.
usa=args.original.read_bytes();assert hashlib.sha256(usa).hexdigest()=='fa8cacf5bbfc39ee6bbaa557adf89133d60d42f6cf9e1db30d5a36a469f74d15';original=usa[0x6099b:0x6099b+0x400];data=bytearray(original)
for y,x in zip(*np.where(fixed!=a)):
 spr,addr,px,py=mapping[y,x];assert spr>=0,(x,y)
 tileoff=addr-0x3400;assert 0<=tileoff<1024
 n=int(fixed[y,x]);bit=7-px
 for k in range(4):
  off=tileoff+(k//2)*16+py*2+k%2;data[off]=(data[off]&~(1<<bit))|(((n>>k)&1)<<bit)
# No edits to object coordinates, maps, palettes, code or other graphics.
manifest={'placements':placements,'new_ink_pixels':int(newink.sum()),'pixels_outside_wood':len(outside),'minimum_native_margin':float(dist[newink].min()),'source_offset':'0x06099B','source_size':1024,'roms':{}}
for variant in ['TRADUZIDOS','ORIGINAIS']:
 if args.base:
  with zipfile.ZipFile(args.base) as z:base=z.read(f'ROMs/DKC_PTBR_v198_NOMES_{variant}.sfc')
 else:
  from patch_io import apply_ips
  base=apply_ips(usa,(ROOT/f'patches/v198/USA_v1.0_para_v198_{variant}.ips').read_bytes())
 expected={'TRADUZIDOS':'16f5dc6c73f103b558d3e6bdbbed6a31b69ed9a34efc09f29a851c6385eebe84','ORIGINAIS':'ac496c07f08f6e37ccc39e20949047eee1ed0326641f601bd170b00df1242bcc'}
 assert hashlib.sha256(base).hexdigest()==expected[variant]
 rom=bytearray(base);rom[0x6099b:0x6099b+1024]=data
 name=f'DKC_PTBR_v199_NOMES_{variant}.sfc';(OUT/'ROMs'/name).write_bytes(rom)
 changed=[i for i,(x,y) in enumerate(zip(base,rom)) if x!=y];assert all(0x6099b<=i<0x60d9b for i in changed)
 manifest['roms'][variant]={'sha256':hashlib.sha256(rom).hexdigest(),'base_sha256':hashlib.sha256(base).hexdigest(),'bytes_changed':len(changed)}
for name,idx in [('placa_USA',a),('placa_corrigida_estudo',fixed)]:
 im=pal[idx].copy();im[idx==0]=[35,15,35];Image.fromarray(im).resize((512,576),Image.Resampling.NEAREST).save(OUT/'Capturas'/f'{name}.png')
Image.fromarray(fixed).save(OUT/'Resultados/placa_indices.png');(OUT/'Resultados/build.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps(manifest,indent=2))
