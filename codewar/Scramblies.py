"""Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
Notes:
Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.

scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""
s1 = "iigphlasljlfb"
s2 = "afsbhgla"
p1 = 'rkqodlw'*10000
p2 = 'world'*500

def scramble(s1, s2):
    if len(s2) == 0:
        return True
    elif len(s1) == 0:
        return False
    elif len(set(s1)) == len(s1) and len(set(s2)) == len(s2):
        return set(s2) - set(s1) == set()
    elif s1.count(s1[0]) > 1 and s2.count(s2[0]) > 1 and int(len(s1)/s1.count(s1[0])) == len(s1[:s1.index(s1[0], 1)]) and int(len(s2)/s2.count(s2[0])) == len(s2[:s2.index(s2[0], 1)]):
        return set(s2) - set(s1) == set()
    else:
        count = 0
        s_2 = sorted(s2)
        s_1 = sorted(s1)
        for i in range(len(s_2)):
            for j in range(len(s_1)):
                if s_2[i] == s_1[j]:
                    count += 1
                    if i < len(s_2) - 1:
                        i += 1
                    else:
                        break
            return count == len(s2)

print(scramble(s1, s2))


# def scramble(s1,s2):
#     for c in set(s2):
#         if s1.count(c) < s2.count(c):
#             return False
#     return True