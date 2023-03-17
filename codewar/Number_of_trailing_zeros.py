number = 10000000

def zeros(number):
    import math
    sum = 0
    for i in range(1, number):
        arg = number / math.pow(5, i)
        if arg > 1:
            sum += math.floor(arg)
        else:
            break
    return sum
print(zeros(number))
