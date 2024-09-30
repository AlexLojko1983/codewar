'''
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse
the 2-d array in a clockwise snailshell pattern.
NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
'''

array = [[1, 2, 3, 10],
         [4, 5, 6, 11],
         [7, 8, 9, 12],
         [13, 14, 15, 16]]


def snail(array):
    expected = []
    top = 0
    left = 0
    bottom = len(array) - 1
    right = len(array) - 1
    if not array[0]:
        return expected
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            expected.append(array[top][i])
        top = top + 1
        for i in range(top, bottom + 1):
            expected.append(array[i][right])
        right = right - 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                expected.append(array[bottom][i])
            bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    expected.append(array[i][left])
                left += 1
    return expected



print(snail(array))

'''
import numpy as np

def snail(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m
'''