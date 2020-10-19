#BattleShips
#Edited by Jeswin V

#random module
import time
from random import randint

intro = "Welcome to Battleships: The game!"

made = "This game is transferred into python by Jeswin V"
chts = "To unlock cheats, delete the # symbol from line 54 and 53"
chance = "You have 4 chances to guess the battleship. This is a single player game. The o letters are the board. X will be displayed when you hit a place unsuccessfully "
#intro
for b in intro:
  print (b, end = "")
  time.sleep(.08)
print()
for a in made:
  print (a, end = "")
  time.sleep(.1)
print()
for c in chts:
  print (c, end = "")
  time.sleep(.1)
print()
for d in chance:
  print (d, end = "")
  time.sleep(.1)
print ()
print ()

board = []
#code for making the board.Edited by Jeswin for better functionality.
for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)
#using the random module here
ship_row = random_row(board)
ship_col = random_col(board)

#CHEATS GIVEN BELOW#
#print ("Enemy ship row is " + ship_row)
#print ("Enemy ship column is " + ship_col)
#CHEATS GIVEN ABOVE#


#for loop for giving exactly 4 turns
for turn in range(4):
  print ("Turn", turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))


# conditional statement ladder with nested conditional statements
  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sank my battleship!")
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print ("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    if (turn == 3):
      print ("Game Over")
    print_board(board)
