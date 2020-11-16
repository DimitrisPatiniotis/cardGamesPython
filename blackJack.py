import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
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


class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

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
    
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

game_on = True

while game_on:
    # Setting the Deck
    used_deck = Deck()
    used_deck.shuffle()


    dealer_hand = Hand()
    dealer_hand.add_card(used_deck.deal_one())
    dealer_hand.add_card(used_deck.deal_one())

    print("The dealer has drown " + str(dealer_hand.cards[0]))

    player_hand = Hand()
    player_hand.add_card(used_deck.deal_one())
    player_hand.add_card(used_deck.deal_one())
    print("\nPlayer has drown " + str(player_hand.cards[0]) + " and " + str(player_hand.cards[1]))
    print("Player score is " + str(player_hand.value))

    play = True

    while play:
        player_choice = input("\nPress h to hit or s to stand")

        if player_choice == 'h':
            player_hand.add_card(used_deck.deal_one())
            print("Player has drown " + str(player_hand.cards[-1]))
            player_hand.adjust_for_aces()
            print("Player's score is " + str(player_hand.value))
            if player_hand.check_loss():
                print('Your score is over 21. Unlucky!')
                game_on = False
                break
        elif player_choice == 's':
            print("Player's score is " + str(player_hand.value))
            print("Dealer's second card is " + str(dealer_hand.cards[1]))
            dealer_hand.adjust_for_aces()
            print("Dealer score is " + str(dealer_hand.value))
            
            dealer_turn = True

            while dealer_turn:
                if dealer_hand.value <= player_hand.value:
                    dealer_hand.add_card(used_deck.deal_one())
                    print("\nDealer has drown " + str(dealer_hand.cards[-1]))
                    dealer_hand.adjust_for_aces()
                elif dealer_hand.value > 21:
                    print("Dealer over 21! You win!")
                    play = False
                    game_on = False
                    break
                else:
                    print("Dealer wins with a score of " + str(dealer_hand.value))
                    play = False
                    game_on = False
                    break