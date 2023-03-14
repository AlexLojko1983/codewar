"""In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.
alphabet_position("The sunset sets at twelve o' clock.") "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
"""
text = "The sunset sets at twelve o' clock."


# def alphabet_position(text):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     listText = list(text.lower())
#     newtext = ''
#     while not text.isalpha():
#         for i in listText:
#             if not i in list(alphabet):
#                 listText.remove(i)
#         text = ''.join(listText)
#         if not text:
#             return newtext
#
#     for i in listText[:-1]:
#         newtext += str(alphabet.find(i) + 1) + ' '
#     newtext += str(alphabet.find(listText[-1])+1)
#     return newtext

s = "The sunset sets at twelve o' clock."

def alphabet_position(s):
  return ' '.join(str(ord(c)-ord('a')+1) for c in s.lower() if c.isalpha())

print(alphabet_position(text))
print(alphabet_position(s))
