'''
For a given list [x1, x2, x3, ..., xn] compute the last (decimal) digit of x1 ^ (x2 ^ (x3 ^ (... ^ xn))).
E. g., with the input [3, 4, 2], your code should return 1 because 3 ^ (4 ^ 2) = 3 ^ 16 = 43046721.
Beware: powers grow incredibly fast. For example, 9 ^ (9 ^ 9) has more than 369 millions of digits.
lastDigit has to deal with such numbers efficiently.
Corner cases: we assume that 0 ^ 0 = 1 and that lastDigit of an empty list equals to 1.
This kata generalizes Last digit of a large number; you may find useful to solve it beforehand.
'''


# def last_digit(lst):
#     if len(lst) == 0: return 1
#     elif len(lst) == 1: return lst[0]
#
#     elif len(lst) == 2:
#         for i in range(len(lst)):
#             return pow(lst[0],lst[1],10)
#     return pow(lst[0], pow(lst[1], lst[2]), 10)


def last_digit(lst):
    if len(lst) == 0: return 1
    elif len(lst) == 1: return lst[0]
    new_value = pow(lst[-2], lst[-1], 10)
    if len(lst) == 2 and lst[1] == 1:
        return lst[0]
    elif len(lst) == 2 and lst[1]!=1:
        lst = lst[:-2] + [new_value]
        return last_digit(lst)
    lst = lst[:-2] + [new_value]
    return last_digit(lst)

print(last_digit([499942, 898102, 846073]))
