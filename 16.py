#16
while True:
    print("a^n")
    try:
        a = int(input("a: "))
        b = int(input("b: "))
        num = a**b
        print(num)
        num_list = list(str(num))
        Sum_num = 0
        for i in num_list:
            i = int(i)
            Sum_num+=i
        print("sum: ", end="")
        print(Sum_num)
        break
    except ValueError:
        print("write the number")