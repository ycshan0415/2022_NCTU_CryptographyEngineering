import math

ct = 'EOEYE GTRNP SECEH HETYH SNGND DDDET OCRAE RAEMH TECSE USIAR WKDRI RNYAR ANUEY ICNTT CEIET US'
ct = ct.replace(" ", "")

ans1 = 0
for r in range(7):
    sum = 0
    avg = 0.4 * 11
    for c in range(11):
        if ct[r + 7 * c] in "AEIOU":
            sum += 1
    diff = abs(sum - avg)
    ans1 += diff          
# print("7 rows, 11 columns:", ans)

ans2 = 0
for r in range(11):
    sum = 0
    avg = 0.4 * 7
    for c in range(7):
        if ct[r + 11 * c] in "AEIOU":
            sum += 1
    diff = abs(sum - avg)
    ans2 += diff
# print("11 rows, 7 columns:", ans)
if ans1 < ans2:
    print('7 rows, 11 columns')
else:
    print('11 rows, 7 columns')
# 11 rows, 7 columns

refer = 'WITHM ALICE TOWAR DNONE WITHC HARIT YFORA LLWIT HFIRM NESSI NTHER IGHTA SGODG IVESU STOSE\
ETHER IGHTL ETUSS TRIVE ONTOF INISH THEWO RKWEA REINT OBIND UPTHE NATIO NSWOU NDSTO CAREF ORHIM WHOSH\
ALLHA VEBOR NETHE BATTL EANDF ORHIS WIDOW ANDHI SORPH ANTOD OALLW HICHM AYACH IEVEA NDCHE RISHA JUSTA\
NDLAS TINGP EACEA MONGO URSEL VESAN DWITH ALLNA TIONS GREEC EANNO UNCED YESTE RDAYT HEAGR AGREE MENTW\
ITHTR UKEYE NDTHE CYPRU STHAT THEGR EEKAN DTURK ISHCO NTING ENTSW HICHA RETOP ARTIC IPATE INTHE TRIPA\
RTITE HEADQ UARTE RSSHA LLCOM PRISE RESPE CTIVE LYGRE EKOFF ICERS NONCO MMISS IONED OFFIC ERSAN DMENA\
NDTUR KISHO FFICE RSNON COMMI SSION EDOFF ICERS ANDME NTHEP RESID ENTAN DVICE PRESI DENTO FTHER EPUBL\
ICOFC YPRUS ACTIN GINAG REEME NTMAY REQUE STTHE GREEK ANDTU RKISH GOVER NMENT STOIN CREAS EORRE DUCET\
HEGRE EKAND TURKI SHCON TINGE NTSIT ISAGR EEDTH ATTHE SITES OFTHE CANTO NMENT SFORT HEGRE EKAND TURKI\
SHCON TINGE NTSPA RTICI PATIN GINTH ETRIP ARTIT EHEAD QUART ERSTH EIRJU RIDIC ALSTA TUSFA CILIT IESAN\
DEXEM PTION SINRE SPECT OFCUS TOMSA NDTAX ESASW ELLAS OTHER IMMUN ITIES ANDPR IVILE GESAN DANYO THERM\
ILITA RYAND TECHN ICALQ UESTI ONSCO NCERN INGTH EORGA NIZAT IONAN DOPER ATION OFTHE HEADQ UARTE RSMEN\
TIONE DABOV ESHAL LBEDE TERMI NEDBY ASPEC IALCO NVENT IONWH ICHSH ALLCO MEINT OFORC ENOTL ATERT HANTH\
ETREA TYOFA LLIAN CE'

refer = refer.replace(' ', '')
trigram = {}
for i in range(len(refer) - 2):
    tri = refer[i] + refer[i + 1] + refer[i + 2]
    if tri not in trigram:
        trigram[tri] = 1
    else:
        trigram[tri] += 1
bigram = {}
for i in range(len(refer) - 1):
    bi = refer[i] + refer[i + 1]
    if bi not in bigram:
        bigram[bi] = 1
    else:
        bigram[bi] += 1

w = {}
for triKey in trigram:
    biKey = triKey[0:2]
    for biKey in bigram:
        weight = math.log(26 * (trigram[triKey] / bigram[biKey]))
        w[triKey] = weight


columns = []
# GRE...
for i in range(7):
    column = ''
    for j in range(11):
        column += ct[j + 11 * i]
    columns.append(column)

columns.remove('GNDDDDETOCR')
columns.remove('RNYARANUEYI')
pt = []
pt.append('GNDDDDETOCR')
pt.append('RNYARANUEYI')

for i in range(5):
    maxProb = 0
    for column in range(len(columns)):
        prob = 0
        for j in range(11):
            pre = pt[i][j] + pt[i + 1][j]
            # two letters(columns) before
            # pt[column][row]
            # same row, different column
            cur = pre + columns[column][j]
            # check which column is the best choice
            if cur in w:
                prob += w[cur]
        if prob > maxProb:
            maxProb = prob
            bestCol = columns[column]
    columns.remove(bestCol)
    pt.append(bestCol)

str = ''
for row in range(11):
    for column in range(7):
        str += pt[column][row]
print(str)