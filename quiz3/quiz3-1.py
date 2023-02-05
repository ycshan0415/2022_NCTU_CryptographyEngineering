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

m = input()
# m = m.replace(" ", "")
# m = m.strip()
keylen = 0
diff = 1
for n in range(4, 8):
    if (abs(check(n, m) - 0.66) < diff):
        diff = abs(check(n, m) - 0.66)
        keylen = n
print(keylen)
