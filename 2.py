#1
x = int(input("sum_of_elements: "))
num = 0
full_list = []
even_list = []
while True:
    full_list.append(num)
    if num%2 == 0:
        even_list.append(num)
    elif len(even_list) == x:
        print(full_list)
        print(even_list)
        print(sum(even_list))
        break
    if num == 0:
        num = 1
    else:
        num = full_list[-1] + full_list[-2]
