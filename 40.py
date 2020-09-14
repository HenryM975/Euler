#40
fullist = []
for num in range(1, 1000000):
    fullist.append(num)
    if num == 10:
        fullist.append(1)
print(fullist)
result = fullist[0] * fullist[9] * fullist[999] * fullist[9999] * fullist[99999] * fullist[999999]
print(result)




