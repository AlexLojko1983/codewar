'''
For a given list [x1, x2, x3, ..., xn] compute the last (decimal) digit of x1 ^ (x2 ^ (x3 ^ (... ^ xn))).
E. g., with the input [3, 4, 2], your code should return 1 because 3 ^ (4 ^ 2) = 3 ^ 16 = 43046721.
Beware: powers grow incredibly fast. For example, 9 ^ (9 ^ 9) has more than 369 millions of digits.
lastDigit has to deal with such numbers efficiently.
Corner cases: we assume that 0 ^ 0 = 1 and that lastDigit of an empty list equals to 1.
This kata generalizes Last digit of a large number; you may find useful to solve it beforehand.
'''


def last_digit(lst):
    if len(lst) == 0: return 1
    if len(lst) == 1: return lst[0]
    return pow(lst[0], pow(lst[1], lst[2]), 10)


print(last_digit([937640, 767456, 981242]))
