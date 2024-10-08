'''
Your task is to sort a given string. Each word in the string will contain a single number.
This number is the position the word should have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input string is empty, return an empty string. The words in the input
String will only contain valid consecutive numbers.
'''


def order(sentence):
    if len(sentence) == 0:
        return ''
    result = [[] for _ in range(len(sentence.split(' ')))]
    sentence = sentence.split(' ')
    for i in range(len(sentence)):
        for j in sentence[i]:
            if j.isdigit():
                result[int(j)-1] = sentence[i]
    return ' '.join(result)


sentence = "is2 Thi1s T4est 3a"
print(order(sentence))
