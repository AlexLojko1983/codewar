'''
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing second character of the
final pair with an underscore ('_').

Examples:
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
'''


def solution(s):
    if len(s) % 2 != 0: s = s + '_'
    s_split = [x for x in s]
    result = []
    for i in range(len(s_split)-1, -1,-1):
        if i % 2 == 0:
            result.append(s_split[i])
            result.append(' ')
        else:
            result.append(s_split[i])

    result.reverse()
    res = ''.join(result).rstrip().split(' ')

    return res[1:]

print(solution('abcdefj'))
