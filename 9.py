#9
lista = []
listb = []
listc = []
for a in range(300):
    for b in range(300):
        for c in range(300):
            if a**2 + b**2 == c**2 and a + b + c == 1000:
                lista.append(a)
                listb.append(b)
                listc.append(c)
print("a: " + lista)
print("b: " + listb)
print("c: " + listc)
if lista == []:
    print("no result")