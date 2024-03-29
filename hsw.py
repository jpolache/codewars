'''
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
'''
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
    
print(high('yxhxhlsml wnxahuhzsa a man i need a ixat taxi up to ubud')) #'taxi'  
    
'''
def high(x):
    word_score_dict = {}
    max_word = ""
    max_word_score = 0
    for word in (x.split(" ")):
        score = 0
        for letter in word:
            score += ord(letter)-96
        print(word, str(score))
        word_score_dict[word] = score
    for key in word_score_dict:
        if word_score_dict[key] > max_word_score:
            max_word_score = word_score_dict[key] 
            max_word = key
    return max_word
        



test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
test.assert_equals(high('take me to semynak'), 'semynak')
'''
