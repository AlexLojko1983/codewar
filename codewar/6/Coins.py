def coins(coin1, coin2):
    if coin1 % 2 and coin2 % 2:
        return -1
    elif not coin1 % 2 and not coin2 % 2:
        return -1
    else:
        if coin1<coin2:
            f = coin1 - 1
        else:
            f= coin2 -1
        a= list(range(coin1*10 + coin2*10))
        for n in range(31):
            for l in range(31):
                c=coin1*n + coin2*l
                if a.count(c)!=0:
                    a.remove(c)
        print(a)
        f= max(a)

        return f


print(coins(11, 18))
