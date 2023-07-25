def count_primes_less_than(N: int) -> int:
    primes = [True] * (N+1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= N:
        if primes[p]:
            for i in range(p * p, N+1, p):
                primes[i] = False
        p += 1

    prime_numbers = []
    for i in range(2, N+1):
        if primes[i]:
            prime_numbers.append(i)

    return len(prime_numbers)

print(count_primes_less_than(340000))
