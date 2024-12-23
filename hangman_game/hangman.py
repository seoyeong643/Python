# portfolio project: hangman game

from hangman_figure import figure

print(
"""
      ☾☁︎                                 _______
    ☁︎                            ☁︎       |     |
                __                       |     O
|__|  /\  |\ | / _`  |\/|  /\  |\ |      |    /|\\
|  | /~~\ | \| \__>  |  | /~~\ | \|      |    / \\
_________________________________________|_________                                          
""")

assigned_word = "unknown word"
unknown_word = ""
wrong_guess = 0
guessed_letters = []

for char in range(0, len(assigned_word), 1):  # char in assigned_word:
    if assigned_word[char] != " ":
        unknown_word += "_"
    else:
        unknown_word += " "

# def update_word(assigned_word: str, unknown_word:str, guess: str):
#     x=""
#     for char in range(0, len(assigned_word), 1):
#         if assigned_word[char] == guess[0]:
#             x+=guess[0]
#         elif unknown_word[char] == " ":
#             x+=" "
#         elif unknown_word[char] == "_":
#             x+="_"
#         else:
#             x+=unknown_word[char]
#     unknown_word = x


while True:
    print(f"number of wrong guesses: {wrong_guess}/6")
    figure(wrong_guess)

    print(f"unknown word: {unknown_word}")                      #______
    print(f"guessed letters: {guessed_letters}")                #list of guessed letters by the user
    guess = input("guess a letter of the word: ").lower()
    print()
    if len(guess)!=1 or not guess.isalpha():                    #isalpha: a-z
        print("guess 'a letter' of the word\n\n")
        continue
    
    if guess in guessed_letters:
        print(f"you have already guessed {guess}\n\n")
        continue

    if guess in assigned_word:
        print(f"the unknown word does contain the letter {guess}.")
        # unknown_word = update_word(assigned_word, unknown_word, guess)
        x=""
        for char in range(0, len(assigned_word), 1):
            if assigned_word[char] == guess[0]:
                x+=guess[0]
            elif unknown_word[char] == " ":
                x+=" "
            elif unknown_word[char] == "_":
                x+="_"
            else:
                x+=unknown_word[char]
        unknown_word = x
        
            
    else:
        print(f"the unknown word does not contain the letter {guess}.")
        wrong_guess+=1
    
    if "_" not in unknown_word:
        print(f"you have correctly guessed the assigned word '{assigned_word}'. good job.")
        exit()

    if wrong_guess == 6:
        print(f"\nyou died. the word was {assigned_word}. good job.")
        figure(wrong_guess)
        exit()

    guessed_letters += guess
    print()
    print()

