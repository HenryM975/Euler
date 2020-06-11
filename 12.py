#12
num = 1
numlist = [1]
while True:
    num += 1
    sumnum = numlist[-1] + num
    numlist.append(sumnum)
    clearnumlist = []
    for i in range(1,100):
        clearnumlist.append(i)
    dellist = []
    for i in clearnumlist:
        if sumnum % i == 0:
            dellist.append(i)
    lendellist = len(dellist)
    print("----------------")
    print(num)
    print("num: ")
    print(sumnum)
    print("dellist: ")
    print(dellist)
    if lendellist == 6:
        break
print("OVER")
print(num)
print(dellist)
print("***********************************")