""" Task: Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing
second character of the final pair with an underscore ('_').
"""

text = "asdfadsf"


def solution(text):
    if len(text) % 2 != 0:
        text += '_'
    text_list = list(text)
    new_text = []
    for i in range(0, len(text_list), 2):
        new_text.append(text_list[i] + text_list[i + 1])
        i += 2
    return new_text


print(text)

print(solution(text))
