import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    x = input("\nEnter to pick a card, or Q plus enter to quit: ")
    if(x == "Q"):
        print("Goodbye")
        break
    else:
        random_card = random.choice(diamonds)
        diamonds.remove(random_card)
        hand.append(random_card)
        print(f"Your hand: {hand}")
        print(f"Remaining cards: {diamonds}")


if not diamonds:    #diamnds list is empty
    print("There are no more cards left.")