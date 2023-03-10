""" Task: Write a function that takes in a string of one or more words,
 and returns the same string, but with all five or more letter words reversed
 (Just like the name of this Kata). Strings passed in will consist of only letters and spaces.
 Spaces will be included only when more than one word is present.
"""

sentence = 'Single word'
def spin_words(sentence):
    a = sentence.split()
    for i in range(len(a)):
        if len(a[i]) >= 5:
            a[i] = a[i][::-1]
    return ' '.join(a)
print(spin_words(sentence))
