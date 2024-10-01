'''
Given two positive integers m (width) and n (height), fill a two-dimensional list (or array) of size m-by-n in
the following way:
(1) All the elements in the first and last row and column are 1.
(2) All the elements in the second and second-last row and column are 2, excluding the elements from step 1.
(3) All the elements in the third and third-last row and column are 3, excluding the elements from the previous steps.
And so on ...
'''

def create_box(m, n):  ## m and n positive integers
    lst = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0 or i == m-1 or j == n-1:
                 lst[i][j] = 1
            else:
                lst[i][j] = 2
    return lst

print (create_box(5,8))