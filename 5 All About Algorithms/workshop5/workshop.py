"""
            ---------- Task One ----------

    Guess the Number by User Input:
        -Create a game where you have to guee a random number
         within a certain range of integers.
        -The game will always tell you whether your guess was too high or too low.
        -Report to the User how many tries they have left and stop the game
         when they have guessed the number or have no tries left.
        -import the 'random' library to randomly pick a number.

"""

import random


def guess_random_num(tries: int, low_bound: int, upper_bound: int) -> None:
    
    random_num = random.randint(low_bound, upper_bound)

    while tries: 
        print(f"Number of tries: {tries}")
        guess = int(input(f"Guess a number between {low_bound} and {upper_bound}: "))
        if guess == random_num:
            print("You guessed the correct number !")
            return
        elif guess < random_num:
            print("Guess Higher!")
        else:
            print("Guess lower !")
        tries -= 1
        print()

    print(f"You have failed to guess the number {random_num}")

#guess_random_num(10, 1, 100)


"""
            ---------- Task Two ----------

    Guess the Number Computer Linear Search:
        - Create a game where a program does the search for you.
        - The search algorithm must run in O(n) - Linear Time

"""

def guess_random_num_linear(tries: int, lower_bound: int, upper_bound: int) -> None:
    random_num = random.randint(lower_bound, upper_bound)

    print(f"The number for the program to guess is: {random_num}")

    for num in range(lower_bound, upper_bound):

        if not tries:
            print(f"The program failed to guess the number: {random_num}")
            return

        print(f"Number of tries left: {tries}")
        print(f"The program is guessing...{num}")

        if num == random_num:
            print(f"The program guessed the correct number: {random_num}")
            return

        tries -= 1

#guess_random_num_linear(100000, 1, 200000)


"""
            ---------- Task Three ----------

    Guess the Number Computer Linear Search:
        - Create a game where a program does the search for you.
        - The search algorithm must run in O(log(n)) - Logarithmic Time

"""

def guess_random_num_binary(lower_bound: int, upper_bound: int) -> None:

    random_num = random.randint(lower_bound, upper_bound)
    print(f"Random number to find is: {random_num}")
    binary_tries = 0

    while True:
        pivot = (lower_bound + upper_bound) //2

        if pivot == random_num:
            print(f"Found the number {random_num}!")
            return binary_tries

        elif pivot > random_num:
            print("Guess Lower!")
            upper_bound = pivot -1

        else:
            print("Guess Higher!")
            lower_bound = pivot +1           

        binary_tries += 1

    #print(f"Your program failed to find the number... {random_num}")

num_tries = guess_random_num_binary(1, 1000)

print(f"It took {num_tries} to complete the search.")