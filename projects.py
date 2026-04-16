import random
words = ["apple","brain","code"]
word = random.choice(words)
guessed = []
attempts = 6
while attempts>0:
    print("Word:", "".join([c if c in guessed else "_" for c in word]))
    letter = input("Guess: ")
    if letter in word:
        guessed.append(letter)
    else:
        attempts -= 1
    if all(c in guessed for c in word):
        print("You win!")
        break
    else:
        print("You lose! Word was:", word)
