"""Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
which is the number of times you must multiply the digits in num until you reach a single digit.
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)
  """

number = int(input('Input m: '))
def persistence(number):
    import math
    def listing(number):
        l_num = []
        while number > 0:
            l_num.append(number % 10)
            number //= 10
            l_num.reverse()
        return l_num
    count = 0
    while len(listing(number)) > 1:
        number = math.prod(listing(number))
        count += 1
    return count

print(persistence(number))

