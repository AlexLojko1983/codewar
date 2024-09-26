'''An isogram is a word that has no repeating letters,
consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.'''


def is_isogram(string: str):
    for i in range(len(string)):
        if string[i + 1:].lower().find(string[i].lower()) != -1: return False
    return True


print(is_isogram("Dermatoglyphics"))
