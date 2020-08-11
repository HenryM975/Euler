#32
finallist = []
for num in range(100000):
    numlist = list(str(num))
    lenlist = len(numlist)
    numlist.sort()
    print(numlist)
    checklist = []
    for numpart in range(1, lenlist+1):
        checklist.append(str(numpart))
    print(checklist)
    print("-------")
    checklist.sort()
    if checklist == numlist:
            finallist.append(num)
print(finallist)
#?
flist = []
for first in range(1, 100):
    for second in range(1, 200):
        for third in range(1, 10000):
            part_of_flist = []
            split_list = []
            if first * second == third:
                split_list.append(first)
                split_list.append(second)
                split_list.append(third)
                #print(split_list)
                sf_list = []
                for part in split_list:
                    for element in str(part):
                        sf_list.append(element)
                #print(sf_list)
                num_len = len(sf_list)
                int_sf_list = []
                for element in sf_list:
                    int_element = int(element)
                    int_sf_list.append(int_element)
                sorted_int_sf_list = sorted(int_sf_list)
                list_of_len_sf_list = []
                for len_element_part in range(len(sf_list)):
                    list_of_len_sf_list.append(len_element_part)
                #print(sorted_int_sf_list)
                #print(list_of_len_sf_list)
                #print("-----------------")
                if sorted_int_sf_list == list_of_len_sf_list:
                    print(first)
                    print(second)
                    print(third)
                    print("+++++++++++")
                    part_of_flist.append(first)
                    part_of_flist.append(second)
                    part_of_flist.append(third)
                    flist.append(part_of_flist)
print(flist)






        
