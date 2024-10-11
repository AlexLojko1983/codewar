'''
Your friend just purchased a share on a stock for S_0 = 100 dollars.
(All numbers presented are examples and will vary in the coding task.)
Alas, he's now worried that the investment might lose its value.
To hedge against this risk, your friend asks you to insure him against future loss of value.
Specifically, after T = 52 weeks, if the share price S_T has dropped below S_0, you compensate him the difference S_0 - S_T.

How much should you charge for such insurance? You have decided to value the insurance by its expected compensation at time T.
(This ignores time value of money, but is appropriate in a zero interest rate environment.)

After each week, you expect the stock to either go up by a factor of u = 1.02 with probability p = 0.495,
or down by a factor of d = 1 / u otherwise. This yields a simulation procedure — a discrete "random walk" —
from which you can derive the final share price S_T and thus the realized insurance compensation.

Task
Given S_0, T, u and p, calculate the value of the insurance; that is, the expected insurance compensation.

The number of weeks T is always an integer between 1 and 52 * 5 = 260, inclusive. Remember,
the simulation is discrete in time, with the stock price changing each week.
'''
import numpy as np

def insurance_value(S_0, T, u, p):
    d = 1 / u
    compen = []
    for i in range(10000):
        S = S_0
        for j in range(T):
            if np.random.rand() < p:
                S *= u
            else:
                S *= d
        if S_0 > S:
            com = S_0 - S
        else:
            com = 0
        compen.append(round(com,4))
    return round(np.mean(compen),4)


print(insurance_value(100, 52, 1.02, 0.495))
