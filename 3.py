#3
final_num = int(input("write final num: "))
divider_list = []
list_of_prime_factors = []
full_list = []
for num in range(1, final_num):
    #full_list.append(num)
    if final_num % num == 0:
        divider_list.append(num)
        """
            for num2 in range(1, num-1):
                if num % num2 != 0:
                    list_of_prime_factors.append(num)
print(list_of_prime_factors)
"""
print(divider_list)