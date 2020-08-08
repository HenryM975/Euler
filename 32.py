#32
finallist = []
for num in range(30):
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
    
        
