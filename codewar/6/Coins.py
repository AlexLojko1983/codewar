def coins(coin1, coin2):
    if not coin1%2 and not coin2%2:
        return -1
    elif coin1<coin2:
        f = coin1 - 1
    else:
        f= coin2 -1
    a= set(range(coin1*50 + coin2*50))
    # print(a)
    c = list()
    for n in range(100):
        for l in range(100):
            c.append(coin1*n + coin2*l)
            # print(c)
            b= a.difference(set(c))

    print(b)
    print(max(a))
    if len(b)==0:
        return -1
    elif len(b)>len(a)//2:
        return -1
    else:
        f= max(b)
        return f

print(coins(51, 24))
