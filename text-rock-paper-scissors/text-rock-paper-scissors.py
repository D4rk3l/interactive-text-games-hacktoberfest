# Text based rock paper scissors
import random

class Player:
    ''' Class that represents a your opponent in the game'''

    def __init__(self):
        self.score = 0 # player keeps track of his score
        self.move = None # player's current move
        self.choices = ['rock', 'paper', 'scissors'] # player options

    def make_choice(self):
        ''' Prompt the player for a decision'''
        valid_input = False
        while valid_input == False:
            decision = input(f"What is your move?\n(Type one of the following: {self.choices}): ")
            if decision in self.choices:
                valid_input = True
            else: 
                print(f"You entered {decision}. That is not a valid input")
        
        self.move = decision

class Opponent(Player):
    '''Opponent class that inherits from Player class'''

    def make_move(self):
        ''' Choose a move at random to play'''
        choice = random.randint(0,2)
        self.move = self.choices[choice]

def start_game():
    '''Main program to run the game'''
    print('=' * 40)
    print('Welcome to Rock, Paper, Scissors!')
    print('=' * 40)

    # Create the cpu and current player
    p1 = Player()
    cpu = Opponent()

    # Keep playing until player doesn't want to play anymore
    play_again = True
    while play_again:
        # players cast their move
        p1.make_choice()
        cpu.make_move()

        print(f"Your opponent played: {cpu.move}")

        # Evaluate win or loss
        if p1.move == cpu.move:
            print("It is a draw! Rematch time...")
            print("=" * 40)
        elif p1.move == 'rock' and cpu.move == 'scissors':
            print("You win!")
            print("=" * 40)
            p1.score += 1
        elif p1.move == 'paper' and cpu.move == 'rock':
            print("You win!")
            print("=" * 40)
            p1.score += 1
        elif p1.move == 'scissors' and cpu.move == 'paper':
            print("You win!")
            print("=" * 40)
            p1.score += 1
        else:
            print("You lose!")
            print("=" * 40)
            cpu.score += 1

        print(f'Your Score: {p1.score}')
        print(f'Opponent Score: {cpu.score}')

        # Ask if they want to keep playing
        print("=" * 40)
        valid_feedback = False
        while valid_feedback == False:
            feedback = input("Play again? (Y)es or (N): ")
            if feedback == 'N':
                play_again = False
                valid_feedback = True
            elif feedback == 'Y':
                valid_feedback = True
            else:
                print("Invalid input! (Enter Y or N)")



if __name__=="__main__":
    start_game()