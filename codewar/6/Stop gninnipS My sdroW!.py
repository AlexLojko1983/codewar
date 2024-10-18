'''
Write a function that takes in a string of one or more words, and returns the same string, but with all words that have
five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
'''

def spin_words(sentence):
    result = []
    for word in sentence.split(' '):
        if len(word) >= 5:
            word = word[::-1]
        result.append(word)
    return ' '.join(result)


sentence = "Hey fellow warriors"
print(spin_words(sentence))

'''
def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
'''