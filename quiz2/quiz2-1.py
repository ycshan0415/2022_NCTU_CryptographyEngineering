text = "ECDTM ECAER AUOOL EDSAM MERNE NASSO DYTNR VBNLC RLTIQ LAETR IGAWE BAAEI HOR"
text = text.replace(" ", "")

ans = 0
for r in range(7):
    sum = 0
    avg = 3.6
    for c in range(9):
        if text[r + 7 * c] in "AEIOU":
            sum += 1
    diff = abs(sum - avg)
    ans += diff          
print("7 rows, 9 columns:", ans)


l = []
ans = 0
for r in range(9):
    sum = 0
    avg = 2.8
    for c in range(7):
        if text[r + 9 * c] in "AEIOU":
            sum += 1
    diff = abs(sum - avg)
    ans += diff
print("9 rows, 7 columns:", ans)