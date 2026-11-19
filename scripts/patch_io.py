"""Leitura e aplicação de IPS em memória; não contém dados de ROM."""

def records(data):
    if data[:5] != b'PATCH':
        raise ValueError('Cabeçalho IPS inválido')
    pos = 5
    while True:
        if data[pos:pos+3] == b'EOF':
            pos += 3
            if pos != len(data):
                raise ValueError('Dados extras após EOF; este projeto usa IPS sem truncamento')
            return
        if pos + 5 > len(data):
            raise ValueError('Registro IPS incompleto')
        offset = int.from_bytes(data[pos:pos+3], 'big')
        size = int.from_bytes(data[pos+3:pos+5], 'big')
        pos += 5
        if size:
            payload = data[pos:pos+size]
            if len(payload) != size:
                raise ValueError('Payload IPS incompleto')
            pos += size
        else:
            if pos + 3 > len(data):
                raise ValueError('Registro RLE incompleto')
            size = int.from_bytes(data[pos:pos+2], 'big')
            if not size:
                raise ValueError('Registro RLE vazio')
            payload = bytes([data[pos+2]]) * size
            pos += 3
        yield offset, payload


def apply_ips(original, patch):
    result = bytearray(original)
    for offset, payload in records(patch):
        if offset + len(payload) > len(result):
            raise ValueError('Patch fora dos limites da ROM de origem')
        result[offset:offset+len(payload)] = payload
    return bytes(result)
