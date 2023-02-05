dict = {}
for i in range(26):
    dict[chr(ord("A") + i)] = 0
text = "K YZWLNKXKJWGN QUGN ETNMX MPLMZOMXYM K TMMJOXA XEN TKZ ZMQEBMF TZEQ KJKZQ EX KXKJWDOXA KXF MPLJEZM NHM TJEEF ET XMI CXEIJMFAM IHOYH MKYH WMKZ RZOXAG IONH ON"
for key in dict:
    dict[key] = text.count(key)
for key in dict:
    print(key, ":", dict[key])