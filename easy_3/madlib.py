import os

WORDS_NEEDED = [
    'plural noun',
    'plural noun',
    'verb',
    'adjective',
    'adverb',
    'past tense verb'
    ]

def prompt(message=""):
    print(f"==> {message}")

def story(words):
    prompt("Madlibs!")
    prompt()
    print(
        f"I woke up and it was raining like {words[0].lower()} and \n"
        f"{words[1].lower()}. I couldn't {words[2].lower()} out the \n"
        f"{words[3].lower()} window! {words[4].capitalize()}, no one was \n"
        f"{words[5].lower()}."
        )
    prompt()

def get_words():
    words = []
    for need in WORDS_NEEDED:
        prompt(f"Enter a {need}:")
        word = input()

        while not word.isalpha():
            prompt(f"Enter one word that is a {need}.")
            word = input()

        words.append(word)
    return words

def run_madlib():
    print()
    prompt("Welcome to Madlibs!\nIf you've never played before it's easy.\n"
           "Simply enter a one word response for the type of word requested."
           "\nYou'll be asked to enter 6 words. "
           "Then you get to read the Madlib!")
    print()
    submitted = get_words()
    os.system('clear')
    story(submitted)

run_madlib()