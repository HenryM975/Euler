#33
for denominator in range(1, 100):
    for numerator in range(1, 100):
        den_list = list(str(denominator))
        num_list = list(str(numerator))
        for element1 in den_list:
            for element2 in num_list:
                if element1 == element2:
                    den_list.remove(element1)
                    num_list.remove(element2)
        print(den_list)
        print(num_list)
        denominator = float(denominator)
        numerator = float(numerator)
        fraction = numerator/denominator#???
        if fraction < 1 and fraction > 0:
            print(fraction)

