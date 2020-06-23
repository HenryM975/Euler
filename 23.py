#23
perfect_number_list = []
for num in range(1,100):
    divider_list = []
    for divnum in range(1,num):
        if num % divnum == 0:
            divider_list.append(divnum)
    print(num)
    print(divider_list)
    if sum(divider_list) == num:
        perfect_number_list.append(num)
print(perfect_number_list)

