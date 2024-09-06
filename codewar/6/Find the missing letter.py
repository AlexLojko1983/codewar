# Write a method that takes an array of consecutive (increasing) letters as input and
# that returns the missing letter in the array.
# You will always get an valid array. And it will be always exactly one letter be missing.
# The length of the array will always be at least 2.
# The array will always contain letters in only one case.


def find_missing_letter(chars):
    for i in range(len(chars)-1):
        if ord(chars[i+1]) != ord(chars[i])+1:
            return chr(ord(chars[i])+1)
    pass
#
print(find_missing_letter(['a','b','c','d']))
# alphabet = [chr(i) for i in range(97, 123)]
# print(''.join(alphabet).find(''.join(['a','b','c','d'])))
# print(''.join(alphabet))
# print(''.join(['a','b','c','d','f']))