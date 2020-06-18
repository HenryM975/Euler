#20
try:
    num = int(input("n: "))
    final_num = 1
    for i in range(1, num + 1):
        final_num *= i
    print("n! =", end=" ")
    print(final_num)
except ValueError:
    print("write the number")