#22
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabet_dict1 = {}
alphabet_dict2 = {}
Final_dict = {}
num = 0
for i in alphabet:
    num += 1
    alphabet_dict1[i] = num
    big_i = i.upper()
    alphabet_dict2[big_i] = num
for letter in alphabet_dict2:
    if letter not in alphabet_dict1:
        alphabet_dict1.setdefault(letter, alphabet_dict2[letter])
#make dict with "a":1 "A":1 connection of two pronounced dictionary
open_file = open('22data')
rf = open_file.read()
name_list = rf.split(",")
name_list = sorted(name_list)
for name in name_list:
    name_letters = list(name)
    letters_num_sum = 0
    for name_letter in name_letters:
        for part in alphabet_dict1:
            if name_letter == part:
                letters_num_sum += alphabet_dict1[part]
    name_index = name_list.index(name) + 1
    final_num = letters_num_sum * name_index
    Final_dict[name] = final_num
print(Final_dict)
