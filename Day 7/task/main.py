import random

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
import hangman_words
lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
print(hangman_art.logo)
# print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []
guessed = False

while not game_over:
    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f'You currently have {lives} lives left for this game.')
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    display = ""

    if guess not in guessed_letters:
        guessed_letters.append(guess)
        guessed = False
    else:
        print(f'The letter {guess.upper()} has already been submitted. Try a different letter')
        guessed = True

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    # print(guessed_letters)
    # print(correct_letters)

    print("Word to guess: " + display)

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word and guessed == False:
        lives -= 1
        print(f"You guessed {guess.upper()}, that's not in the word. You lose a life")

        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"Big Loser. The word you were guessing was {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    print(hangman_art.stages[lives])
