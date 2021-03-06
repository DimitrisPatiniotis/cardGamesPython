import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
blackJackValues = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


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

    # Shuffling cards
    def shuffle(self):
        random.shuffle(self.all_cards)

    # Dealing 1 deck card
    def deal_one(self):
        return self.all_cards.pop()

class Player():

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    #Drawing 1 card
    def remove_one(self):
        return self.all_cards.pop(0)

    #For war game
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # List of multiple cards
            self.all_cards.extend(new_cards)
        else:
            # For a single card
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

class BlackJackHand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += blackJackValues[card.rank]

        if card.rank  == 'Ace':
            self.aces += 1
    
    def adjust_for_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
    
    def check_loss(self):
        return self.value > 21

class Chips():

    def __init__(self, total):
        self.total = total
        self.bet = 0

    def place_bet(self):
        self.bet = int(input(f'Please place your bet (your total is {self.total})\n'))
    
    def win_bet(self):
        self.total += self.bet
        # Reseting betting size
        self.bet = 0

    
    def lose_bet(self):
        self.total -= self.bet
        # Reseting betting size
        self.bet = 0