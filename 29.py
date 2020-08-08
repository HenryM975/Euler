#29
full_list = []
final_list = []
for num in range(2, 100):
    for num1 in range(2, 100):
        num3 = num**num1
        full_list.append(num3)
for element in full_list:
    if element not in final_list:
        final_list.append(element)
print(sorted(final_list))
