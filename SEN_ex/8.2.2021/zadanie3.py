from collections import Counter

login = []

f = open('zadanie3txt.txt', 'r')

for line in f:
    line = line.strip()
    login.append(line)

pocet_loginov = Counter(login).most_common()

# napíše počet loginov, ktoré sa vyskytli v zozname,
print('celkový pocet prihlaseni bol:\t', len(login))

for i in pocet_loginov:  # - napíše počet loginov, ktoré sa vyskytli v zozname,
    print(i[0], 'sa pripojil ', i[1], 'x')

print("najvacsi pocet loginov mal:\t", pocet_loginov[0][0])
