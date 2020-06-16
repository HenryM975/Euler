#14
try:
    first_num = int(input("first num: "))
    last_num = int(input("last_num: "))
    maxlen = 0
    for i in range(first_num, last_num + 1):
        list1 = []
        startnum = i
        print("***")
        while True:
            print(i)
            list1.append(i)
            if i % 2 == 0:
                i /= 2
            elif i <= 1:
                if len(list1) > maxlen:
                    maxlen = len(list1)
                    num = startnum
                break
            else:
                i = 3 * i + 1
    print("maxlen:")
    print(maxlen)
    print("startnum:")
    print(num)
except ValueError:
    print("write the number")
