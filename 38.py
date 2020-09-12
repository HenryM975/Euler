#38
comparison_list_main = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in range(200):    
    testlist = []
    comparison_list_local = []
    for factor  in range(1, 4):
        composition = num * factor
        testlist.append(composition)
    r = "".join(map(str, testlist))
    print(r)
    print(testlist)
    for element in r:
        comparison_list_local.append(int(element))
    if sorted(comparison_list_local) == comparison_list_main:
        print("fine!")

