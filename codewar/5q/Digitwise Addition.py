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
#     return len(str(s))

def digitwise_addition(n, k):
    lst = [_ for _ in str(n)]
    count = len(lst)
    for i in range(len(lst)):
        delta = 10 - int(lst[i])
        '''
        1. Если delta = k, надо добавить 1
        2. Если delta < k и k-delta меньше 10, +1
        3. Если delta < k и k-delta больше 10, +//10
        4. Если остаток от деления больше или = дельте, +1
        '''
        if delta <= k and k - delta < 10:
            count += 1
        elif delta < k and k - delta >= 10:
            count += 1 + (k - delta) // 10
        if k - delta >= 10 and delta <= (k - delta) % 10:
            count += 1
    return count


print(digitwise_addition(433365377, 14))

# n=433365377 and k=14
