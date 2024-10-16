'''
Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
For example, the score of abad is 8 (1 + 2 + 1 + 4).
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.
'''
a = 'aa b'


def high(x):
    dict_x = {}
    for i in x.split(' '):
        key = 0
        for j in i:
            key += (ord(j)-96)
        if key not in dict_x.keys():
            dict_x[key] = i
    print(dict_x)
    return dict_x[max(dict_x.keys())]


print(high(a))

'''
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
'''
