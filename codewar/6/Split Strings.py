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
    result = s.split()
    for i in range(len(s)):
        if i%2 == 0:
            result.insert(i,' ')
    return result


print(solution('abcdefj'))
