#23
perfect_number_list = []
excess_number_list = []
for num in range(1,100):#28123
    divider_list = []
    for divnum in range(1,num):
        if num % divnum == 0:
            divider_list.append(divnum)
    if sum(divider_list) > num:
        excess_number_list.append(num)
excess_number_sum_list = []
for i in range(100):#28123
    for part1 in excess_number_list:
        for part2 in excess_number_list:
            if part1 != part2:
                part_sum = part1 + part2
                excess_number_sum_list.append(part_sum)
final_list = []
for i in range(100):#28123
    if i not in excess_number_sum_list:
        final_list.append(i)
print(final_list)
print(sum(final_list))


