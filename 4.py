#4
firstlist = []
for i in range(10,100):
    for j in range(10, 100):
        a = i*j
        k = list(str(a))
        num1 = k[0]
        num2 = k[-1]
        p = len(str(a))
        if num1 == num2 :
            if p <= 3:
                firstlist.append(a)
            elif p >= 4:
                num3 = k[1]
                num4 = k[-2]
                if num3 == num4:
                    firstlist.append(a)#возможно усовершенствование путем автоматизации для поиска чисел любого размера
o = max(firstlist)
print(firstlist)
print("max: " , o)
print("len: " , p)