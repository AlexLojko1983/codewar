"""Task: Implement a function that accepts 3 integer values a, b, c.
The function should return true if a triangle can be built with the sides of given length and false in any other case."""
a = 1
b = 1
c = 2


def Triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a
