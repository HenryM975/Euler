#41
n = 3
finallist = []
while True:
    divider_list = []
    for num in range(2, n):
        if n % num == 0:
            divider_list.append(num)
    if divider_list == []:
        finallist.append(n)
    n+=1
    if n == 100:
        break
print(finallist)





