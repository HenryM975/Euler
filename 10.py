#10
list = []
secondlist = []
thirdlist = []
for i in range(20000):
     secondlist.append(i)
     if i % 2 == 0 or i % 3 == 0 or i % 4 == 0 or i % 5 == 0:
         list.append(i)
     elif i == 100:
         print("100")
     elif i == 1000:
         print("1000")
for j in secondlist:
    if j not in list:
        thirdlist.append(j)
print(list)
print(secondlist)
print(thirdlist)
print(sum(thirdlist))