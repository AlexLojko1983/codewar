'''
In this little assignment you are given a string of space separated numbers,
and have to return the highest and lowest number.
'''


def high_and_low(numbers: str):
    numbers = numbers.split(' ')
    max = int(numbers[0])
    min = int(numbers[0])

    for digit in numbers:
        if int(digit) > max:
            max = int(digit)
        if int(digit) < min:
            min = int(digit)
    return f'{max} {min}'.format(max, min)


'''
def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
'''
print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))