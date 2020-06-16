#18
list = [3, 7, 4, 2, 4, 6, 8, 5, 9, 3]
list2 = []
n = 0
m = 1
l = 2
while True:
    list2.append(list[n:m])
    print(list2)
    n = m
    m += l
    l+=1
    if len(list2) == 4:
        break
sum = 0
for part in list2:
    max_num = max(part)
    sum+=max_num
    print(sum)
print(sum)