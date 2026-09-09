import random

words = ["Road", "Rain", "Ramp", "Roof", "Rice"]

secret_word = random.choice(words).lower()
guessed = set()
wrong_guesses = 0
max_wrong = 6

print("=== Hangman Game ===")
print("Hint: The word starts with 'R' and has 4 letters.")

while wrong_guesses < max_wrong:
    # Show the word with underscores for unguessed letters
    display = " ".join(letter if letter in guessed else "_" for letter in secret_word)
    print(f"\nWord: {display}   |   Wrong guesses: {wrong_guesses}/{max_wrong}")
    if "_" not in display:
        print(" You guessed the word! You win!")
        break
    guess = input("Guess a letter: ").strip().lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed:
        print("You already guessed that letter.")
        continue
    if guess in secret_word:
        print("Correct!")
        guessed.add(guess)
    else:
        print("Wrong!")
        wrong_guesses += 1
        guessed.add(guess)
if wrong_guesses == max_wrong:
    print(f"\n Game over! The word was: {secret_word}")