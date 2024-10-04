'''
Digitwise addition is a special kind of addition where instead of adding 1 normally to the number,
it adds 1 to every digit of that number. If the digit is a 9, we replace it with a 10 without carrying over to the next digit.
'''

n = 1322
s= str(n)
print(s.split(' '))

def digitwise_addition(n, k):
    # Test Constraints:
    # 1 <= n <= 10 ** 9
    # 1 <= k <= 10 ** 5
    # Expected Time Complexity: O(k * log(n))
    return 0