#25
list = [1, 1]
while True:
    num = list[-1] + list[-2]
    list.append(num)
    len_str_num = len(str(list[-1]))
    if len_str_num >= 100:
        break
print(list)
print("#",end='')
print(len(list)+1)
print(list[-1])