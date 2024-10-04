'''
Digitwise addition is a special kind of addition where instead of adding 1 normally to the number,
it adds 1 to every digit of that number. If the digit is a 9, we replace it with a 10 without carrying over to the next digit.
'''


# def digitwise(n):
#     lst_end = [str(int(x)+1) for x in [_ for _ in str(n)]]
#     return ''.join(lst_end)
#
# def digitwisestr(s):
#     lst_end = [str(int(x)+1) for x in s]
#     return ''.join(lst_end)
#
#
# def digitwise_addition(n, k):
#     if k == 1: return len(digitwise(n))
#     s = digitwise(n)
#     for i in range(k-1):
#         s = digitwisestr(s)
#     return (s)



def digitwise_addition(n, k):
    import sys
    sys.set_int_max_str_digits(10 ** 6)

    def add_one_to_digits(x):
        result = 0
        multiplier = 1
        while x > 0:
            digit = x % 10
            x //= 10
            if digit == 9:
                result += 10 * multiplier
                multiplier *= 100
            else:
                result += (digit + 1) * multiplier
                multiplier *= 10
        return result

    for _ in range(k):
        n = add_one_to_digits(n)

    return len(str(n))
#
#
print(digitwise_addition(143948553, 16))

# n=143948553 and k=16; 35 should equal 32.
9887878721101098732213221
