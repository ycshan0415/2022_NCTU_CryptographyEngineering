def check(k, m):
    #keylen, mes    
    sub = []
    for s in range(k):
        sub.append("")
    for i in range(len(m)):
        sub[i % k] += m[i]
        
    dict = {}
    icTot = 0
    for j in range(k):
        for d in range(26):
            dict[chr(ord("A") + d)] = 0
        ic = 0
        l = 0
        for key in dict:
            dict[key] = sub[j].count(key)
            ic += dict[key] * (dict[key] - 1)
            l += dict[key]
        ic = ic / (l * (l - 1))
        icTot += ic
    icAvg = icTot / k
    return icAvg

def split(k, m):
    # keylen, mes
    sub = []
    for s in range(k):
        sub.append('')
    for i in range(len(m)):
        sub[i % k] += m[i]
    return sub

def count(m):
    dict = {}
    for d in range(26):
        dict[chr(ord('A') + d)] = 0
    for key in dict:
        dict[key] = m.count(key)
    return dict

def decrypt(kl, sub, m):
    # keylen, groups
    key = ''
    for j in range(kl):
        dict = count(sub[j])
        shift = 0
        icmax = 0
        for k in range(26):
            # shift k bits
            ic = 0
            for i in range(26):
                ic += prob[chr(ord('A') + i)] * dict[chr(ord('A') + (i + k) % 26)]
            if ic > icmax:
                icmax = ic
                shift = k
        key += chr(ord('A') + shift)        
    print(key)
    """
    pt = ''
    for n in range(len(m)):
        group = n % kl
        letter = key[group]
        shift = (ord(m[n]) - ord(letter)) % 26
        # shift left(back)
        pt += chr(ord('A') + shift)
    print(pt)
    """
prob = {}
for d in range(26):
    prob[chr(ord("A") + d)] = 0
prob['A'] = 8.167
prob['B'] = 1.492
prob['C'] = 2.782
prob['D'] = 4.253
prob['E'] = 12.702
prob['F'] = 2.228
prob['G'] = 2.015
prob['H'] = 6.094
prob['I'] = 6.966
prob['J'] = 0.153
prob['K'] = 0.772
prob['L'] = 4.025
prob['M'] = 2.406
prob['N'] = 6.749
prob['O'] = 7.057
prob['P'] = 1.929
prob['Q'] = 0.095
prob['R'] = 5.987
prob['S'] = 6.327
prob['T'] = 9.056
prob['U'] = 2.758
prob['V'] = 0.978
prob['W'] = 2.360
prob['X'] = 0.150
prob['Y'] = 1.974
prob['Z'] = 0.074

m = input()
keylen = 0
diff = 1
for n in range(4, 8):
    if (abs(check(n, m) - 0.66) < diff):
        diff = abs(check(n, m) - 0.66)
        keylen = n
sub = split(keylen, m)
decrypt(keylen, sub, m)

