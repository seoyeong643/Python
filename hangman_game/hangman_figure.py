#creates figure for hangman

def figure(wrong_guess: int):
    if wrong_guess == 0:
        print("_______\n|     |\n|      \n|        \n|        \n|")    #empty
    elif wrong_guess == 1:
        print("_______\n|     |\n|     O\n|        \n|        \n|")
    elif wrong_guess == 2:
        print("_______\n|     |\n|     O\n|     |  \n|        \n|")
    elif wrong_guess == 3:
        print("_______\n|     |\n|     O\n|    /|  \n|        \n|")
    elif wrong_guess == 4:
        print("_______\n|     |\n|     O\n|    /|\\\n|        \n|")
    elif wrong_guess == 5:
        print("_______\n|     |\n|     O\n|    /|\\\n|    /   \n|")
    elif wrong_guess == 6:
        print("_______\n|     |\n|     O\n|    /|\\\n|    / \\\n|_________")
    else:
        print("guess exceeded 6, error")
