#37
finallist = []
for num in range(1, 100):
    divider_list = []
    for divider in range(2, num):
        if num % divider == 0:
            divider_list.append(divider)
    print(divider_list)
    if divider_list == []:
        finallist.append(num)
print(finallist)



