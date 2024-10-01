'''
Let's pretend your company just hired your friend from college and paid you a referral bonus.
Awesome! To celebrate, you're taking your team out to the terrible dive bar next door and using the referral bonus to buy,
and build, the largest three-dimensional beer can pyramid you can.
And then probably drink those beers, because let's pretend it's Friday too.
A beer can pyramid will square the number of cans in each level - 1 can in the top level, 4 in the second,
9 in the next, 16, 25...
Complete the beeramid function to return the number of complete levels of a beer can pyramid you can make,
given the parameters of:
1.your referral bonus, and
2.the price of a beer can
'''


def beeramid(bonus, price):
    count_beer = int(bonus / price)
    count = 0
    i = 1
    while count_beer >= 0:
        count_beer -= i ** 2
        if count_beer >= 0:
            count += 1
        i += 1
    return count


print(beeramid(9, 2))

'''
def beeramid(bonus, price):
    beers  = bonus // price
    levels = 0
    
    while beers >= (levels + 1) ** 2:
        levels += 1
        beers  -= levels ** 2
    
    return levels
'''
