'''Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has
no positive divisors other than 1 and itself.

Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out.
Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.'''

import math
def is_prime(num):
    if num < 2: return False
    for i in range(2, int(round(math.sqrt(num)))+1):
      if num%i == 0:
          return False
    return True

print(is_prime(11))

'''import gmpy2

def is_prime(num):
  return gmpy2.is_prime(num) if num > 0 else False'''