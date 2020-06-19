#17
Element_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
Element_dict = {}
dict_keys = 0
for num in Element_list:
    print(len(num))
    dict_keys += 1
    Element_dict[dict_keys] = len(num)
print(Element_dict)
sum = 0
for i in range(100):
    for key in Element_dict:
        if i == key:
            print(i)
            sum += Element_dict[key]
        if i > 20 and i<30 :
            loc_list = list(str(i))
            if int(loc_list[1]) == key:
                  word_len = Element_dict[20] + Element_dict[key]
                  print(i, end=":")
                  print(word_len)
                  sum += word_len



print(sum)