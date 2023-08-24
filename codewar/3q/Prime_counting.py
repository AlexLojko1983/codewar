def count_primes_less_than(N: int) -> int:
    if N <= 10000000:
        primes = [True] * (N + 1)
        primes[0] = primes[1] = False

        p = 2
        while p * p <= N:
            if primes[p]:
                for i in range(p * p, N + 1, p):
                    primes[i] = False
            p += 1
        return primes.count(True)
    else:
        primes = [True] * (N + 1 - 10000000)
        print(len(primes))
        p = 2
        while p * p <= N - 10000000 + 1:
            if primes[p]:
                for j in range(len(primes)):
                    for i in range(10000001, N + 1):
                        if i % p == 0:
                            primes[j] = False
                        j += 1
                    p += 1

        return primes.count(True) + 664579


print(count_primes_less_than(10000010))

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
