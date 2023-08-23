def count_primes_less_than(N: int) -> int:
    if N < 10000000:
        primes = [True] * (N + 1)
        primes[0] = primes[1] = False

        p = 2
        while p * p <= N:
            if primes[p]:
                for i in range(p * p, N + 1, p):
                    primes[i] = False
            p += 1
        prime_numbers = []
        for i in range(2, N + 1):
            if primes[i]:
                prime_numbers.append(i)

        return len(prime_numbers)
    else:
        primes = [True] * (N + 1 )
        p = 2
        while p * p <= N:
            if primes[p]:
                for i in range(10000000, N + 1):
                    if i % p == 0 and primes[i]:
                        primes[i] = False
            p += 1
        prime_numbers = []
        for i in range(10000000, N + 1):
            if primes[i]:
                prime_numbers.append(i)
        return len(prime_numbers)+664579


print(count_primes_less_than(10000009))

# import math
#
# def sieve_of_eratosthenes(n):
#     primes = [True] * (n + 1)
#     primes[0] = primes[1] = False
#
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if primes[i]:
#             for j in range(i * i, n + 1, i):
#                 primes[j] = False
#
#     return [i for i in range(n + 1) if primes[i]]
#
# lower_bound = 10**7
# upper_bound = 10**10
#
# primes = sieve_of_eratosthenes(upper_bound)
# result = [prime for prime in primes if prime >= lower_bound]
#
# print(result)
#
# print(sieve_of_eratosthenes(999))
