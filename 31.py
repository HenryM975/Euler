#31
coins = [1, 2, 10, 20, 50, 100, 200]
serial_number = 0
money_list = []
combination_list = []
while True:
    money_list.append(coins[serial_number])
    if sum(money_list) == 200:
        serial_number += 1
        combination_list.append(money_list)
        if len(money_list) == 1:
            break
        money_list = []
print(combination_list)
#?