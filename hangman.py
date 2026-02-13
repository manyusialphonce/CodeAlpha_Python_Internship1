import random

# List of predefined words
words = ["python", "coding", "intern", "alpha", "program"]
word = random.choice(words)

guessed_letters = []
attempts = 6

print("Welcome to Hangman Game")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

    print("\nWord:", display)
    print("Attempts left:", attempts)

    if "_" not in display:
        print("Congratulations! You guessed the word.")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct guess!")
    else:
        guessed_letters.append(guess)
        attempts -= 1
        print("Wrong guess!")

if attempts == 0:
    print("Game Over! The word was:", word)