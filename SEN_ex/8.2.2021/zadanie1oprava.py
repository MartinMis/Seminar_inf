from collections import Counter
f = open("zadanietxt1.txt", "r")

input, zakazdnici, zakazdnici_unikat, suma_final, dsa = [], [], [], [], []

for line in f:  # nacita input
    if line == "5\n":
        pass
    else:
        line = line.split(" ")
        line[0], line[1] = int(line[0]), int(line[1])
        input.append(line)
        zakazdnici.append(line[0])
input.sort()

for predaj in input:  # nacita unique zakazdnikov
    if predaj[0] in zakazdnici_unikat:
        pass
    else:
        zakazdnici_unikat.append(predaj[0])

pocet_nakupov = Counter(zakazdnici).most_common()  # zpocita kolko krat zakazdnik v inpute
pocet_nakupov.sort()

x, y = 0, 0
for i1 in range(len(pocet_nakupov)):
    suma = 0
    for i2 in range(pocet_nakupov[i1][1]):
        suma += input[x][1]
        x += 1
    suma_final.append([suma, y])
    y += 1
suma_final.sort(reverse=True)
maxi = suma_final[0][0]

for i in suma_final:
    if i[0] == maxi:
        dsa.append(i[1])
for i in range(len(zakazdnici_unikat)):
    print('zakaznik', pocet_nakupov[i][0], 'nakupoval:\t', pocet_nakupov[i][1], 'x')
print('najviac nakupov:\t', pocet_nakupov[0][0])
for i in range(len(dsa)):
    print("najvaic utratil", pocet_nakupov[dsa[i]][0],)
