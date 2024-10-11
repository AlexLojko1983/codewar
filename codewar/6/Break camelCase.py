'''
Complete the solution so that the function will break up camel casing, using a space between words.
'''

def solution(s):
    result = [i if not i.isupper() else (' '+i) for i in s]
    return ''.join(result)

print(solution('fhfjhlKda'))