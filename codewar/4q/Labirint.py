"""You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions
(i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.
Empty positions are marked ..
Walls are marked W.
Start and exit positions are empty in all test cases."""

import math


def path_finder(maze: str):
    b = maze.split('\n')
    y = 0
    x = 0
    n = len(b)
    while x != n-1 and y != n-1:
        if maze[y][x+1] == '.':
            x +=1
        elif maze[i - 1] == '.' and maze[i - 5] == '.' and i - 5 > 0:
            x = i - 5
            i -= 5
        elif maze[i] == 'W' and maze[i + 5] == '.' and i < len(maze) - 5:
            x = i + 5
            i += 5


a = "\n".join([
    ".W...",
    ".W...",
    ".W.W.",
    "...W.",
    "...W."])


def matrix(a):
    n = math.sqrt(len(a))


b = a.split('\n')
# # print(a[6])
# path_finder(a)
print(len(b))
print(a.split('\n'))
print(math.sqrt(len(a)))
print(b[2][3])
