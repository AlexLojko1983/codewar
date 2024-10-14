'''
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)
1 -->  1
2 --> 3 + 5 = 8
'''


def row_sum_odd_numbers(n):
    list_of_numbers = [i for i in range(1, n + n ** 2) if i % 2 != 0]
    list_of_numbers.reverse()
    return sum(list_of_numbers[:n])


print(row_sum_odd_numbers(13))
'''
def row_sum_odd_numbers(n):
    #your code here
    return n ** 3
'''