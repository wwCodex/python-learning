import random
import hangman_words
import hangman_art
print(hangman_art.logo)
lives = 6

chosen_word = random.choice(hangman_words.word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print("You have " + str(lives) + " lives left")
    guess = input("Guess a letter: ").lower()

    display = ""
    if guess in correct_letters:
        print("You already guessed this letter:" + guess)

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print("This letter is not in the word to be guessed: " + guess)

        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************\n The correct word was {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
        exit(0)

    print(hangman_art.stages[lives])
