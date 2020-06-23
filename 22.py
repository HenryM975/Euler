#22
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabet_dict1 = {}
alphabet_dict2 = {}
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
print(rf)
name_list = rf.split(",")
print(name_list)
name_list = sorted(name_list)
print(name_list)
print(alphabet_dict1)
print(alphabet_dict2)
for name in name_list:
    name_letters = list(name)
print(name_letters)
for name_letter in name_letters:
    for part in alphabet_dict1:
        if name_letter == part:
            print(part)
            print(alphabet_dict1[part])