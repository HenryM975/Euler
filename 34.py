#34
final_list = []
for num in range(1000):
    numlist = list(str(num))
    comparison_list = []
    for element in numlist:
        for factor in range(1, int(element)):
            comparison_list.append(factor)
    final_num = 1
    for part in comparison_list:
        final_num *= part
    if num == final_num:
        final_list.append(num)
print(final_list)
