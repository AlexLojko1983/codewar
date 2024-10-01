'''
Given two positive integers m (width) and n (height), fill a two-dimensional list (or array) of size m-by-n in
the following way:
(1) All the elements in the first and last row and column are 1.
(2) All the elements in the second and second-last row and column are 2, excluding the elements from step 1.
(3) All the elements in the third and third-last row and column are 3, excluding the elements from the previous steps.
And so on ...
'''


def create_box(m, n):  ## m and n positive integers
    lst = [[0 for _ in range(m)] for _ in range(n)]
    k = 1
    left = 0
    right = n - 1
    top = 0
    bottom = m - 1
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            for j in range(top, bottom + 1):
                if i == top or j == left or i == right or j == bottom:
                    lst[i][j] = k
        k += 1
        left += 1
        top += 1
        right -= 1
        bottom -= 1
    return lst


print(create_box(5, 8))

'''
def create_box(m, n):  ## m and n positive integers
    return [[min([x+1, y+1, m-x, n-y]) for x in range(m)] for y in range(n)]
'''
