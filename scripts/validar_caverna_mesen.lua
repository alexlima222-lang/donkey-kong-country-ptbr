local frame=0
assert(emu.getMemorySize(emu.memType.snesSaveRam)==2048)
for i=0,2047 do emu.write(i,0,emu.memType.snesSaveRam) end
local dir=os.getenv('DKC_CAPTURE_DIR')
local mode=tonumber(os.getenv('DKC_MODE') or '0')
local shots={[2800]=true,[3000]=true,[3300]=true,[3600]=true,[3900]=true,[4200]=true}
local function dump()
 local prefix=dir..'/frame_'..frame
 local size=emu.getScreenSize();local buf=emu.getScreenBuffer();local core=assert(io.open(prefix..'_core.ppm','wb'))
 core:write('P6\n'..size.width..' '..size.height..'\n255\n')
 for i=1,#buf do local n=buf[i];core:write(string.char((n>>16)&255,(n>>8)&255,n&255)) end;core:close()
 local f=assert(io.open(prefix..'.png','wb'));f:write(emu.takeScreenshot());f:close()
 for _,m in ipairs({'snesVideoRam','snesSpriteRam','snesCgRam','snesWorkRam','snesSaveRam'}) do
  local size=({snesVideoRam=65536,snesSpriteRam=544,snesCgRam=512,snesWorkRam=131072,snesSaveRam=2048})[m]
  local p=assert(io.open(prefix..'_'..m..'.bin','wb'))
  for a=0,size-1 do p:write(string.char(emu.read(a,emu.memType[m]) or 0)) end p:close()
 end
 local s=assert(io.open(prefix..'_state.txt','w'));local state=emu.getState();local keys={}
 for k in pairs(state) do table.insert(keys,k) end;table.sort(keys)
 for _,k in ipairs(keys) do s:write(tostring(k)..'='..tostring(state[k])..'\n') end;s:close();print('CAPTURE',frame)
end
emu.addEventCallback(function() frame=frame+1;if shots[frame] then dump() end;if frame==4220 then print('DONE');emu.stop(0) end end,emu.eventType.endFrame)
emu.addEventCallback(function()
 local b={}
 if frame>=900 and frame<930 then b.start=true end
 if frame>=1450 and frame<1465 then b.a=true end
 if mode>=1 and frame>=1580 and frame<1590 then b.down=true end
 if mode>=2 and frame>=1640 and frame<1650 then b.down=true end
 if (frame>=1750 and frame<1760) or (frame>=2100 and frame<2110) or (frame>=2500 and frame<2510) then b.a=true end
 if frame>=2900 and frame<4200 then b.left=true end
 emu.setInput(b,0);emu.setInput({},1)
end,emu.eventType.inputPolled)
