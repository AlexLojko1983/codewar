""" Task: Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing
second character of the final pair with an underscore ('_').
"""

s = "asdfads"


def solution(s):
    if len(s) % 2 != 0:
        s += '_'
    new_s = []
    for i in range(0, len(s), 2):
        new_s.append(s[i] + s[i + 1])
        i += 2
    return new_s
# def solution(s):
#     if len(s) == 0:
#         return []
#     elif len(s) == 1:
#         return [s + "_"]
#     else:
#         return [s[:2]] + solution(s[2:])

print(s)

print(solution(s))
