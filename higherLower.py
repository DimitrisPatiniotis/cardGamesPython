from cardGameClasses import Card, Deck

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