'''
A format for expressing an ordered list of integers is to use a comma separated list of either
individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'.
The range includes all integers in the interval including both endpoints.
It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly
formatted string in the range format.
'''

# solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
args = [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]


def solution(args):
    strn_end = ''
    strn = ''
    for i in range(0, len(args) - 1):
        if args[i] == args[i + 1] - 1:
            strn += str(args[i]) + '|'
            if i + 2 == len(args):
                strn += str(args[i + 1])
        else:
            strn += str(args[i]) + ','
    strn = strn.split(',')

    for i in strn:
        if i.count('|') == 1:
            m = i.split('|')
            strn_end += m[0] + ',' + m[1] + ','
        elif i.count('|') > 1:
            k = i.split('|')
            strn_end += k[0] + '-' + k[-1] + ','
        else:
            strn_end += i + ','
    print(type(strn_end))
    return strn_end[:-1]


print(solution(args))
