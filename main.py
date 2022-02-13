#Step 5

import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
guessed_letters = ""
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
      print(f"You have already guessed {guess}, guess again!")
    else:
      guessed_letters += guess

      #Check guessed letter
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter

      #Check if user is wrong.
      if guess not in chosen_word:
          print(f"{guess} is not in the word.")
          lives -= 1
          if lives == 0:
              end_of_game = True
              print(f"You lose. The word was {chosen_word}")

      #Join all the elements in the list and turn it into a String.
      print(f"{' '.join(display)}")

      #Check if user has got all letters.
      if "_" not in display:
          end_of_game = True
          print("You win.")

      print(hangman_art.stages[lives])