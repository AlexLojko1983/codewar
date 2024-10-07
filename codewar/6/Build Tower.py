'''
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors.
A tower block is represented with "*" character.
For example, a tower with 3 floors looks like this:
'''


def tower_builder(n_floors):
    return [('*'*(2*i-1)).center(2*n_floors-1) for i in range(1, n_floors+1)]



print(tower_builder(5))

