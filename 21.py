#21
list_of_friendly_couples = []
for i in range(2,1000):
    dividers_list = []
    range_num = i - 1
    for j in range(1, range_num):
        if i%j == 0:
            dividers_list.append(j)
    dividers_sum = sum(dividers_list)
    if dividers_sum <= 1000:
        list_of_friendly_couples.append(i)
        list_of_friendly_couples.append(dividers_sum)

print("sum: ", end="")
print(sum(list_of_friendly_couples))