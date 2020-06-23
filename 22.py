#22
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#make dict with "a":1 "A":1 connection of two pronounced dictionary
open_file = open('22data')
rf = open_file.read()
print(rf)
name_list = rf.split(",")
print(name_list)
name_list = sorted(name_list)
print(name_list)