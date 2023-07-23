def count_primes_less_than(n: int) -> int:
    num = list(range(2, n + 1))
    list_1 = []
    p = 0
    j = 0
    while p <= n ** 0.5:
        p = num[j]
        list_1.append(p)
        for i in range(p, (n + 1) // p + 1):
            # num.remove(p)
            if i * p in num:
                num.remove(i * p)
        num.remove(p)
    return len(list_1)


print(count_primes_less_than(340000))
