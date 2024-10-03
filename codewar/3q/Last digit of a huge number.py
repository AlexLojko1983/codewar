'''
For a given list [x1, x2, x3, ..., xn] compute the last (decimal) digit of x1 ^ (x2 ^ (x3 ^ (... ^ xn))).
E. g., with the input [3, 4, 2], your code should return 1 because 3 ^ (4 ^ 2) = 3 ^ 16 = 43046721.
Beware: powers grow incredibly fast. For example, 9 ^ (9 ^ 9) has more than 369 millions of digits.
lastDigit has to deal with such numbers efficiently.
Corner cases: we assume that 0 ^ 0 = 1 and that lastDigit of an empty list equals to 1.
This kata generalizes Last digit of a large number; you may find useful to solve it beforehand.
'''


# def last_digit(lst):
#     if not lst:
#         return 1
#     if len(lst) == 1:
#         return lst[0] % 10
#
#     # Удаляем все нули перед последним элементом
#     while len(lst) > 1 and lst[-1] == 0:
#         lst.pop()
#
#     # Если после удаления нулей остался только один элемент
#     if len(lst) == 1:
#         return lst[0] % 10
#
#     # Обработка случая, когда последний элемент списка равен 0
#     if lst[-1] == 0:
#         lst[-1] = 4  # 0^0 считается как 1, но для корректного вычисления используем 4
#
#         # Вычисляем эффективный показатель степени вручную
#         exp = 1
#         for i in range(len(lst) - 1, 0, -1):
#             if lst[i] == 0:
#                 exp = 1
#             else:
#                 exp = (lst[i - 1] % 4 + 4) if exp == 0 else (lst[i - 1] % 4 + 4) ** exp % 4
#
#         base = lst[0] % 10
#         result = 1
#         for _ in range(exp):
#             result = (result * base) % 10
#
#         return result

def last_digit(lst):
    if not lst:
        return 1
    if len(lst) == 1:
        return lst[0] % 10

    def effective_exponent(exp):
        if exp == 0:
            return 1
        return exp % 4 if exp % 4 != 0 else 4

        # Обработка случая, когда последний элемент списка равен 0
    if lst[-1] == 0:
        lst[-1] = 4  # 0^0 считается как 1, но для корректного вычисления используем 4

        # Вычисляем эффективный показатель степени

    exp = lst[-1] % 4 + 4 if lst[-1] > 4 else lst[-1]
    for num in reversed(lst[1:-1]):
        if exp == 1:
            exp = num % 4 + 4 if num > 4 else num
        else:
            exp = effective_exponent(num ** exp)
    if exp == 0:
        return 1
    return (lst[0] ** effective_exponent(exp)) % 10


print(last_digit([106413, 947766, 539413, 457946]))
