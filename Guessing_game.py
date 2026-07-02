
secret_word = "secretword"
guess = ""
guess_count = 0
max_guess = 6

while guess != secret_word and guess_count < max_guess:
     guess = input("Guess the secret word: ").lower()
     guess_count += 1
     if guess == secret_word:
          print("You guessed the word and took",guess_count,"attempt(s).")
     elif guess_count == max_guess:
          print("Too many guesses. Try again.")
     else:
          print("Try again.")







