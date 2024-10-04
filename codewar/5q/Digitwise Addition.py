'''
Digitwise addition is a special kind of addition where instead of adding 1 normally to the number,
it adds 1 to every digit of that number. If the digit is a 9, we replace it with a 10 without carrying over to the next digit.
'''


def digitwise(n):
    lst_end = [str(int(x)+1) for x in [_ for _ in str(n)]]
    return ''.join(lst_end)

def digitwisestr(s):
    lst_end = [str(int(x)+1) for x in s]
    return ''.join(lst_end)


def digitwise_addition(n, k):
    if k == 1:  return len(digitwise(n))
    s = digitwise(n)
    for i in range(k-1):
        s = digitwisestr(s)
    return len(str(s))

print(digitwise_addition(1399,2))