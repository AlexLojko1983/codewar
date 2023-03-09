"""Task: Check to see if a string has the same amount of 'x's and 'o's.
 The method must return a boolean and be case insensitive.
 The string can contain any char.
 XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false"""

s = 'zpzpzpp'



def xo(s):
    count_x = 0
    count_o = 0
    start_x = -1
    start_o = -1
    while True:
        start_x = s.lower().find('x', start_x + 1)
        if start_x == -1:
            break
        count_x += 1
        # break
    while True:
        start_o = s.lower().find('o', start_o + 1)
        if start_o == -1:
            break
        count_o += 1
    if count_x == count_o:
        return True
    return False

print(xo(s))