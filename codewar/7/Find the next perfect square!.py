# You might know some pretty large perfect squares. But what about the NEXT one?
# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
# Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
# If the argument is itself not a perfect square then return either -1 or an empty value like None or null, depending on your language. You may assume the argument is non-negative.
import math
print(math.sqrt(121))
print(type(math.sqrt(121)))
print(int(math.sqrt(122))**2 == 122)
# is_integer() !!!
def find_next_square(sq):
    import math
    if int(math.sqrt(sq))**2 == sq: return (int(math.sqrt(sq))+1)**2
    return -1

print(find_next_square(123))