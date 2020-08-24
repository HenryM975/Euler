#36
baselist = []
for num in range(10, 1000):
    numlist = []
    num = list(str(num))
    for element in num:
        numlist.append(int(element))
    revnumlist = list(reversed(numlist))
    print(numlist)
    print(revnumlist)
    if numlist == revnumlist:
        baselist.append(num)
print(baselist)
