#43
Comparison_list = []
pun_numeral_list = []
for num in range(5):
    Comparison_list.append(num)
for nim in range(1000000):
    temporary_list = []
    for element in str(nim):
        temporary_list.append(int(element))
    if sorted(temporary_list) == Comparison_list:
        pun_numeral_list.append(nim)
print("pn:")
print(pun_numeral_list)
print(sorted(temporary_list))
for part in pun_numeral_list:
    second_temporary_list = []
    for num_part in str(part):
        second_temporary_list.append(num_part)
    print(second_temporary_list)
    print("----------------------")
    left_border = 0
    right_border = 3
    dnum = second_temporary_list[left_border:right_border]
    print(dnum)


    

