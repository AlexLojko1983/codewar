'''
How many ways can you make the sum of a number?
In number theory and combinatorics, a partition of a positive integer n,
also called an integer partition, is a way of writing n as a sum of positive integers.
Two sums that differ only in the order of their summands are considered the same partition.
If order matters, the sum becomes a composition. For example, 4 can be partitioned in five distinct ways:
'''


def exp_sum(n):
    # Создаем массив для хранения количества разбиений
    dp = [0] * (n + 1)
    dp[0] = 1  # Есть один способ разложить 0 - не использовать ни одного числа
    # Заполняем массив dp
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
    return dp[n]


