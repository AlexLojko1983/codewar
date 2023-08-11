def coins(coin1,coin2):
    if coin1%2 and coin2%2:
        return -1
    elif not coin1%2 and not coin2%2:
        return -1
    else:
        if coin1 > coin2:
            return coin2-1
        else: return coin1-1
print(coins(2,3))