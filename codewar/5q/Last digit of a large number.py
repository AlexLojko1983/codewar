'''Define a function that takes in two non-negative integers a and
b returns the last decimal digit of a**b. Note that a and b may be very large!
You may assume that the input will always be valid.'''


def last_digit(n1, n2):
    ost_n2 = n2 % 4
    if n2 == 0:
        number = 1
    elif ost_n2 == 0:
        number = n1 ** 4
    else:
        number = n1 ** ost_n2
    return int(str(number)[-1])

'''def last_digit(n1, n2):
    return pow( n1, n2, 10 )'''



