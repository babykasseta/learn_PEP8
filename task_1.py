import math

def calculate(x, y):
    result = 0
    for degree in range(10):
        if degree % 2 == 0:
            result += math.pow(x, degree) / math.factorial(degree)
    result += y
    return result