#3
final_num = int(input("write final num: "))
list_of_prime_factors = [1]
full_list = []
for num in range(2, final_num):
    if final_num % num == 0:
        rubbish_list = []
        for num2 in full_list:
            if num % num2 == 0:
                rubbish_list.append(num2)
        if rubbish_list == []:
            list_of_prime_factors.append(num)
    full_list.append(num)
print(list_of_prime_factors)
#gtyvtyivbyitukloooooooooooooooooooooooooooooooofvtrffdcerdxcerutyfc