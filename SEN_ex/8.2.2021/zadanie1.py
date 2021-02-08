f = open("zadanietxt1.txt", "r")

zakazndici = []

for line in f:
    line = line.strip()
    line = line.split(" ")
    zakazndici.append(line)

zakazndici = zakazndici[1::]

for i in zakazndici:
    for u in range(2):
        i[u] = int(i[u])

zakazndici.sort()

lst = []
count = -1
new = None

for i in zakazndici:
    if i[0] == new:
        xd = i[1]
        lst[count].append(xd)
    elif i[0] != new:
        lst.append(i)
        count += 1
        new = i[0]
lst.sort()

for i in lst:
    print("zakazdnik\t", i[0])

maxi = max(lst, key=len)
print("najviac nakupov\t", maxi[0])

maxi2 = []
for i in lst:
    i = [i[0], sum(i[1:])]
    maxi2.append(i)

maxi3 = []
for i in maxi2:
    maxi3.append(i[::-1])

maxi3.sort(reverse=True)

maxval = maxi3[0][0]

maxi4 = []
for i in maxi3:
    if i[0] == maxval:
        xd = str(i[1])
        maxi4.append(xd)
print('navacsi minaci', ' '.join(maxi4))
