#38
comparison_list_main = [1, 2, 3, 4, 5, 6, 7, 8, 9]
final_list = []
for num in range(100000):
    print(num)
    testlist = []
    comparison_list_local = []
    for factor  in range(1, 100):
        composition = num * factor
        testlist.append(composition)
        r = "".join(map(str, testlist))
        if len(r) == 9:
            for element in r:
                comparison_list_local.append(int(element))
            if sorted(comparison_list_local) == comparison_list_main:
                final_list.append(num)
            break
print(final_list)
