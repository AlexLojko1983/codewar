# A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits,
# each raised to the power of the number of digits in a given base.
# In this Kata, we will restrict ourselves to decimal (base 10).

number = 122


# number_list = [int(i) for i in list(str(number))]
# print(type(number_list[0]))
# print(f'{not(max(number_list) ** len(number_list) > number)},',f'{number} is narcissistic')
# print(f'{not(sum([i ** len(number_list) for i in number_list])) > number)},',f'{number} is narcissistic')
# print(f'{number} is narcissistic')


# def narcissistic(number):
#     number_list = [int(i) for i in list(str(number))]
#     if max(number_list) ** len(number_list) > number or \
#             sum([i ** len(number_list) for i in number_list]) != number:
#         return f'{False}, {number} is narcissistic'
#     return f'{True}, {number} is narcissistic'

def narcissistic(value):
    return value == sum(int(a) ** len(str(value)) for a in str(value))


print(narcissistic(112))
