from cardGameClasses import Card, Deck, BlackJackHand

game_on = True

while game_on:  
    used_deck = Deck()
    used_deck.shuffle()

    dealer_hand = BlackJackHand()
    dealer_hand.add_card(used_deck.deal_one())
    dealer_hand.add_card(used_deck.deal_one())

    print("The dealer has drown " + str(dealer_hand.cards[0]))

    player_hand = BlackJackHand()
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