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
    

    

