# Pull the middle word from a sentence or phrase.
# String input
# Edge cases: empty string, even number of words, two or less words
# more edge: middle word is connected to punctuation.
# output is middle word

def middle_word(phrase):
    phrase = phrase.split()
    if not phrase or len(phrase) < 3:
        return "Please enter a phrase or sentence with at least three words."
    elif len(phrase) % 2 == 0:
        return f"Please enter a phrase with an odd number of words."
    else:
        mid_word_index = (len(phrase) // 2)
        middle_word = phrase.pop(mid_word_index)
        if not middle_word[-1].isalpha():
            middle_word = middle_word.rstrip(",.!?:;'\"")
        return f"The middle word is: {middle_word}"

# Tests     
print(middle_word("John got the coffee today.")) #the
print(middle_word("")) 
print(middle_word("Hi Joe!"))
print(middle_word("John got the coffee this morning."))
print(middle_word("There were two lil pups running in the snow.")) #pups
print(middle_word("Were you, John?")) #you