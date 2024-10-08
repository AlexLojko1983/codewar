'''
You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except
for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
'''


def find_outlier(integers):
    count_2 = 0
    count_1 = 0
    value_2 = 0
    value_1 = 0
    for i in integers:
        if i % 2 == 0:
            count_2 += 1
            value_2 = i
        else:
            count_1 += 1
            value_1 = i

    
    return dict


integers = [2, 4, 6, 8, 10, 3]
print(find_outlier(integers))
