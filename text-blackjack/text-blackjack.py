import random

class PlayingCards:
    '''Class to handle the deck of cards'''
    def __init__(self):
        self.deck = []
        suit = [x for x in range(2, 11)] + ['J', 'Q', 'K', 'A']
        for x in range(4):
            self.deck += suit

    def draw_a_card(self):
        card_index = random.randint(0, len(self.deck))
        return self.deck.pop(card_index)

class Player:
    '''Player that participates in the game'''

    def __init__(self):
        # Dictionary to help compute hand value
        self.translator = {'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        self.hand = []

    def take_card(self, card_value):
        self.hand.append(card_value)

    def show_sum(self):
        hand_value = 0
        for card in self.hand:
            if card in self.translator:
                hand_value += self.translator[card]
            else:
                hand_value += card
        return hand_value

def play_game():
    '''Class to keep track of score, player names, and program flow'''
    
    # Start game and greet
    print("Welcome to blackjack")
    print("Dealing...")

    # Define player and dealer:
    dealer = Player()
    gambler = Player()

    # Initialize deck and deal 2 cards
    deck = PlayingCards()

    for x in range(2):
        dealer.take_card(deck.draw_a_card())
        gambler.take_card(deck.draw_a_card())

    # Display hand, ask if you want to hit or stay
    hit = True
    while hit:
        print(f"Your hand is: {gambler.hand}")
        print("Would you like to (h)it or (s)tay?")
        user_input = input()

        if user_input == 'h':
            gambler.take_card(deck.draw_a_card())
            # if you hit and go over 21, game over
            if gambler.show_sum() > 21:
                print('You busted (Your hand is greater than 21)')
                hit = False
        elif user_input == 's':
            hit = False
        else:
            print("Not a valid input, please type 'h' to draw a new card or 's' to stay")

    # Dealer moves
    while dealer.show_sum() < 21:
        dealer.take_card(deck.draw_a_card())
    if dealer.show_sum() > 21:
        print("Dealer busted")
        
    # Check for a winner
    print(f"Dealer's hand is: {dealer.hand}, ({dealer.show_sum()})")
    print(f"Your hand is: {gambler.hand}, ({gambler.show_sum()})")

    if gambler.show_sum() > 21:
        print("Dealer WINS!")
    elif dealer.show_sum() > 21:
        print("You WIN!")
    elif dealer.show_sum() >= gambler.show_sum():
        print("Dealer WINS!")
    else:
        print("You WIN!")

if __name__=='__main__':
    play_game()
