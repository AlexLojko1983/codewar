'''
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors.
A tower block is represented with "*" character.
For example, a tower with 3 floors looks like this:
'''


def tower_builder(n_floors):
    line = "*" * (2 * n_floors - 1)
    list_lines = [line for _ in range(n_floors)]
    for i in range(n_floors-1):
        
    return list_lines

print(tower_builder(3))