# В этом простом задании вам дается число, и вы должны сделать его отрицательным.
# А может быть, число уже отрицательное?

def make_negative( number ):
    if number<0:
        return number
    elif number>0:
        return -1*number
    return 0

number = 0
print(make_negative(number))

# def make_negative( number ):
#     return -abs(number)
