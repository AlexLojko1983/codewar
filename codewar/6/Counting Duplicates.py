'''
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits
that occur more than once in the input string. The input string can be assumed to contain only alphabets
(both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
'''


def duplicate_count(text):
    dict_text = {i: text.lower().count(i) for i in text.lower()}
    count = sum([1 for i in dict_text.values() if i > 1])
    return count


print(duplicate_count('fgsafhgh465'))

'''
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
'''
