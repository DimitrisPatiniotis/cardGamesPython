import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck():

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))
    
    def shuffle(self):
        return random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop(0)


game_on = True
score = 0

while game_on:

    usedDeck = Deck()
    usedDeck.shuffle()

    dealtCard = usedDeck.deal_one()
    print("The current card is ", dealtCard)
    print("Your score is " + str(score))

    userInput = input("Higher or lower?")

    while userInput != 'h' and userInput != 'l':
        print('Please enter a valid input (h for higher or l for lower)')
        userInput = input("Higher or lower?")
        if userInput == 'h' or userInput == 'l':
            break


    nextCard = usedDeck.deal_one()
    print("The next card is ", nextCard)

    if dealtCard.value == nextCard.value:
        print("It's a tie!")

    elif dealtCard.value > nextCard.value:
        if userInput == 'h':
            print('Wrong answer! Your final score is ' + str(score))
            game_on = False
        elif userInput == 'l':
            print("Correct guess!")
            score += 1 

    else:
        if userInput == 'h':
            print("Correct guess!")
            score += 1
        elif userInput == 'l':
            print('Wrong answer! Your final score is ' + str(score))
            game_on = False