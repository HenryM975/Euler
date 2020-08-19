#35
final_list = []
for num in range(100):
    for divider in range(2, num+1):
        if divider == num:
            final_list.append(num)
        if num % divider == 0:
            break
print(final_list)
