#! Python3
# By Mason Hernandez @ 3LMK
# Black Jack Game

#  Imports and Global Variables

import random
START_GAME = True
COUNT = 0

# setup to create Deck of cards.
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,'Queen': 10, 'King': 10, 'Ace': 11}


#########################################################
#########################################################
###########                           ###################
########### OOP Constructors/Class's  ###################
###########                           ###################
#########################################################
#########################################################

#  Card Class (single card) Allows you to create a single card by passing suit and rank.

class Card():
    def __init__(self, suit, rank):  # creates a single card object
        self.suit = suit
        self.rank = rank
        self.value = values[rank]   # uses dictionary to grab integer value

    def __str__(self):
        return f"{self.rank} of {self.suit}"


#  Deck Class (52 card deck) Allows you to create a full deck of cards.

class Deck:
    def __init__(self):
        self.all_cards = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                the_deck = Card(suit, rank)
                self.all_cards.append(the_deck) # creates a list with a full deck of 52 card objects


    def shuffle(self):
        random.shuffle(self.all_cards) # shuffles the list Deck()

    def deal(self):
        return self.all_cards.pop(0) # remove one card object from top of the deck

    def __str__(self): # prints each card object inside the Deck list.
        deck = ""
        for card in self.all_cards:
            deck += "\n" + card.__str__()
        return f"The Deck has:{deck}"


#  Hand Class (Players hand)

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list to hold the dealt cards
        self.value = 0  # adds the value of each players Hand()
        self.aces = 0  # add a counter to keep track of aces

    def add_card(self, card):
        self.cards.append(card) # after creating a Hand() object allows you to add cards from Deck() object using deal()

        self.value += values[card.rank]  # increasing value from 0 to self.value

        if values[card.rank] == values["Ace"]: # increasing value from 0 to self.aces
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0: # if total value > 21 and you have 1 ace, will turn ace to value to 1 and remove the ace count
            self.value -= 10
            self.aces -= 1

    def __str__(self): # prints your card hand and the value of hand.
        empty = ""
        for card in self.cards:
            empty += "\n" + card.__str__()
        return f"Your hand is: {empty} \nwith a value of: {self.value}"


#  Chips Class (stack of chips)

class Chips:
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):     # adds bet amount won to total
        self.total += self.bet


    def lose_bet(self):   # subrtacts the bet amount lost from total
        self.total -= self.bet


###################################################
###################################################
###########                     ###################
########### Function Defintions ###################
###########                     ###################
###################################################
###################################################

#  function for taking bets

def take_bet(chips): # pass on Chips() object as argument: mybet = Chips() then take_bet(mybet) will deduct amount from your
    while True:
        try:
            chips.bet = int(input("How many Bitcoin's would you like to bet?\n\n"))

        except ValueError: # makes sure user inputs integer value
            print("Sorry you did not input an integer amount!")
            continue

        if chips.bet > chips.total: # check to see if you have enough to make bet
            print(f"Sorry, You do not have enough chips, You only have {chips.total} Bitcoin's")

        else:
            break


# function for taking hits

def hit(deck, hand): # must pass Deck() object and Hand() object
    hand.add_card(deck.deal())  # removes a card from deck and add to hand object
    hand.adjust_for_ace()  # check to see if you have an ACE in case you need it to be 1 instead of 11


#  function prompting the Player to Hit or Stand

def hit_or_stand(deck, hand):
    global START_GAME  # to control an upcoming while loop
    while True:
        answer = input("Would you like to Hit or Stand?\n")
        if answer[0].lower() == "h":
            hit(deck, hand) # hit function from above

        elif answer[0].lower() == "s":
            print("Player Stands. Dealer is Playing\n")
            START_GAME = False

        else:
            print("Please try again! Remember! Enter 'h' for hit and 's' for stand ")
            continue
        break


# functions to display card

def show_some(player, dealer): # player and dealer names are not important can be any name. we pass two Hand() objects
    print("Dealer's Hand:")
    print("<One Card hidden>")
    print(dealer.cards[1]) # only display's the second card dealt to dealer
    print("\nPlayer's Cards:")
    for card in player.cards: # uses Card() class __str__() to print and display all cards value/rank
        print(card)

def show_all(player, dealer):
    print("\nDealer's Hand:")
    for i in dealer.cards:
        print(i)
    print("\nPlayer's Hand:")
    for i in player.cards:
        print(i)

### Step 10: Write functions to handle end of game scenarios

def player_busts(player, dealer, chips):
    print("\nPlayer BUSTS, Dealer Wins!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("\nPlayer Wins!\n")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("\nDealer BUSTS, Player Wins!\n")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("\nDealer Wins!\n")
    chips.lose_bet()


def push(player,dealer):
    print("\nPlayer and Dealer Tie, PUSH\n")


#########################################################################
#########################################################################
##########################                     ##########################
##########################  GAME LOGIC STARTS  ##########################
##########################                     ##########################
#########################################################################
#########################################################################



while True:
    COUNT += 1
    if COUNT < 2:
        print("\nWelcome to Mason's Black Jack Game! Get as close to 21 as you can without going over!\n")  # Print an opening statement
        print("Aces count as 1 or 11")
        my_bet = Chips()  # 100 chips for the player to start with
        print(f"\nPlayer! You have {my_bet.total} Bitcoin's to start!", end=" ")
        take_bet(my_bet)  # Prompt player how much they want to bet?
        print(f"You have made a bet for {my_bet.bet} Bitcoin's\n")
        new_deck = Deck()  # new deck
        new_deck.shuffle()  # shuffle the deck


    player = Hand()  # create a hand for player (each hand() object has an empty list)
    dealer = Hand()  # create a hand for dealer

    for i in range(2):  # add two cards to each Hand() object
        hit(new_deck, player)
        hit(new_deck, dealer)

    show_some(player, dealer) # Show cards (but keep one dealer card hidden)

    while START_GAME:  # recall this variable from our hit_or_stand function (nested loop)
        print("\nPlayer! ", end="")
        hit_or_stand(new_deck, player)  # Prompt for Player to Hit or Stand (breaks out of both play_on loops, is stand)

        show_some(player, dealer) # Show cards (but keep one dealer card hidden)

        if player.value > 21: # If player's hand exceeds 21, run player_busts() and break out of loop
            player_busts(player, dealer, my_bet) # player loses bet
            break # will break out of nested loop

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value <= 21: # make sure player has not Busted
        while dealer.value < 17 or player.value > dealer.value: # keeps adding cards to dealer hand until the value is higher then 17
            hit(new_deck, dealer)

        show_all(player, dealer) # No more dealing, time to check who wins.

        if dealer.value > 21:  # Dealer is over 21 they bust (Player wins)
            dealer_busts(player, dealer, my_bet)  # Player wins bet

        elif dealer.value > player.value:  # Dealer is under 21 and higher hand then player (Dealer wins)
            dealer_wins(player, dealer, my_bet)  # Player loses bet

        elif dealer.value < player.value:  # Player is under 21 and higher hand then Dealer (Player wins)
            player_wins(player, dealer, my_bet) # Player wins bet

        else:
            push(player, dealer)  # They both have same value (PUSH)


    print(f"Player now has a total of {my_bet.total} bitcoins\n") # inform player of chip amount

    if my_bet.total == 0:
        print("You are out of Bitcoin's!! Please come back another day.\n Goodbye! ")
        break

    play_again = input("Would you like to keep playing? Type in Yes or No\n")

    if play_again[0].lower() == "y":
        take_bet(my_bet)  # Prompt player how much they want to bet?
        START_GAME = True
        continue

    else:
        print(f"Thanks for playing! You left with a total of {my_bet.total} Bitcoin's. Have a wonderful day.")
        break  # will break out of the main loop