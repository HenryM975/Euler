i = 13
list1 = []
list2 = ()
for i in range(1,10):
    while True:
        print(i)
        list1.append(i)
        len_list = len(list1)
        if i%2 == 0:
            i /= 2
        elif i <= 1:
            break
            list2.append(list1)
            list2.append("*")
        else:
            i = 3*i + 1
print(list2)