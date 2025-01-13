import random
stages = ["You're dead", "You have one life", "You have two lives", "You have three lives", "You have four lives", "You have five lives"]


word_list = ["angels", "black", "camouflage", "donkey"]
lives = 6
word = random.choice(word_list)
print(word)

# Placeholder for the word
display = "_" * len(word)
print(display)

game_over = False
correct_letters = []

while not game_over:
    # Take the user's guess
    guess = input("Guess a letter: ").lower()

    # Update the display based on the guess
    new_display = ""
    for index, letter in enumerate(word):
        if letter == guess:
            new_display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            new_display += letter
        else:
            new_display += "_"
    display = new_display

    # Show updated display
    print(display)

    if guess not in word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")

    # Check if the game is over
    if "_" not in display:
        game_over = True
        print("You win!")

    print(stages[lives])