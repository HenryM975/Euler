#32
finallist = []
for num in range(10000):
    numlist = list(str(num))
    lenlist = len(numlist)
    print(numlist)
    print(lenlist)
    checklist = []
    for numpart in range(num):
        numpart = str(numpart)
        if numpart in numlist:
            finallist.append(num)
print(finallist)
    
        
    
