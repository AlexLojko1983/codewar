"""  Task: Move the first letter of each word to the end of it,
then add "ay" to the end of the word. Leave punctuation marks untouched.
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
"""

text = 'O tempora o mores !'
def pig_it(text):
    new_text = []
    text1 = ''
    for work in text.split():
        if work.isalpha():
            temp = list(work)
            temp.append(temp.pop(0) + 'ay')
        else:
            temp = list(work)
        work_new = ''    #
        for i in temp:
            work_new += i
        new_text.append(work_new)
    text1 = ' '.join(new_text)
    return text1

print(text)
pig_it(text)
print(pig_it(text))