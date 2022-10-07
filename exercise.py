

def make_division_by(n):
    '''

    This closure returns a function that returns the division of an x number by n

    '''
    def divisor(x):
        return x / n

    return divisor 

divbision_by_3 = make_division_by(3)
print(int (divbision_by_3(18)))

divbision_by_5 = make_division_by(5)
print(int (divbision_by_5(100)))

divbision_by_18 = make_division_by(18)
print(int (divbision_by_18(54)))