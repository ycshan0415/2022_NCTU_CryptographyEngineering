import hashlib
m = hashlib.md5()
hex_val = input('input:')
bytes = bytes.fromhex(hex_val)
m.update(bytes)

h = m.hexdigest()
it = int(hex_val, 16)

while(1):
    m = hashlib.md5()
    it = it + 1
    s = str(hex(it)[2 : ])
    bytes = bytes.fromhex(s)
    m.update(bytes)
    
    h2 = m.hexdigest()
    if (h2[0 : 4] == h[0 : 4]):
        break

print(h2[0 : 4], hex(int(s, 16))[2 : ])
