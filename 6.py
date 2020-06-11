#6
k = int(input("write num: "))
firstlist = []
secondlist = []
for i in range(k):
    j = i ** 2
    firstlist.append(j)
    secondlist.append(i)
sum1 = sum(firstlist)
sum2 = sum(secondlist)
qwsum2 = sum2 ** 2
print(qwsum2)
raz = (qwsum2 - sum1)
print(raz)