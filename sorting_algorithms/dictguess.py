"""Guarantees the correct word guess within 19 guesses"""

words = []
with open("words_alpha.txt", "r") as alpha_dictionary:
    words = alpha_dictionary.read().split("\n")

def guess(words, current_guess):
    ans = input("Is {} the right word? ".format(words[current_guess]))
    next_guess = int((current_guess-1)/2)

    if len(words) < 100:
        print(words)
    
    if ans == '=':
        return
    elif ans == '<':
        guess(words[:current_guess], next_guess)
    elif ans == '>':
        guess(words[current_guess+1:], next_guess)

if __name__ == "__main__":
    current_guess = int((len(words)-1)/2)
    guess(words, current_guess)
