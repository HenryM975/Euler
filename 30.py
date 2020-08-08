#30
limit = int(input("number limit: "))
finallist = []
for num in range(limit):
    numlist = list(str(num))
    summa = 0
    for part in numlist:
        part = int(part)
        summa += part**5
    if num == summa:
        finallist.append(int(num))
print(finallist)
print(sum(finallist))
