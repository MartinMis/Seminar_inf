import random
veta = "Na tomto texte sa pokusime zistit ci hypoteza funguje"

veta = veta.split(" ")

vetarozklad = []
for slovo in veta:
    slovo.split()

for i in veta:
    a = []
    strxd = list(i)
    strxdnew = strxd[1:-1]
    random.shuffle(strxdnew)
    a.extend(strxd[0])
    a.extend(strxdnew)
    a.extend(strxd[-1])
    vetarozklad.append(a)
x = []
for i in vetarozklad:
    x.append(''.join(i))

print(' '.join(x))
