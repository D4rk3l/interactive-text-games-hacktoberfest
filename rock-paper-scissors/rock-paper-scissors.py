import random
from os import system, name

title="""
                 _                                                               _                        
                | |                                                             (_)                       
  _ __ ___   ___| | __  ______   _ __   __ _ _ __   ___ _ __   ______   ___  ___ _ ___ ___  ___  _ __ ___ 
 | '__/ _ \ / __| |/ / |______| | '_ \ / _` | '_ \ / _ \ '__| |______| / __|/ __| / __/ __|/ _ \| '__/ __|
 | | | (_) | (__|   <           | |_) | (_| | |_) |  __/ |             \__ \ (__| \__ \__ \ (_) | |  \__ \
 |_|  \___/ \___|_|\_\          | .__/ \__,_| .__/ \___|_|             |___/\___|_|___/___/\___/|_|  |___/
                                | |         | |                                                           
                                |_|         |_|                                                           
"""

pl_roc = []
pl_pap = []
pl_sci = []

en_roc = []
en_pap = []
en_sci = []


pl_roc.append("    _______                ")
pl_roc.append("---'   ____)               ")
pl_roc.append("      (_____)              ")
pl_roc.append("      (_____)              ")
pl_roc.append("      (____)               ")
pl_roc.append("---.__(___)                ")


pl_pap.append("     _______               ")
pl_pap.append("---'    ____)____          ")
pl_pap.append("           ______)         ")
pl_pap.append("          _______)         ")
pl_pap.append("         _______)          ")
pl_pap.append("---.__________)            ")


pl_sci.append("    ______                 ")
pl_sci.append("---'  ____)_____           ")
pl_sci.append("          ______)          ")
pl_sci.append("       __________)         ")
pl_sci.append("      (____)               ")
pl_sci.append("---.__(___)                ")



en_roc.append("  _______")
en_roc.append(" (____   '---")
en_roc.append("(_____)")
en_roc.append("(_____)")
en_roc.append(" (____)")
en_roc.append("  (___)__.---")


en_pap.append("      _______ ")
en_pap.append(" ____(____    '---")
en_pap.append("(______")
en_pap.append("(_______")
en_pap.append(" (_______")
en_pap.append("   (__________.---")


en_sci.append("        _____")
en_sci.append("  _____(___  '---")
en_sci.append(" (_____")
en_sci.append("(__________")
en_sci.append("      (____)")
en_sci.append("      (___)__.---")


pl_moves = [pl_roc, pl_pap, pl_sci]
en_moves = [en_roc, en_pap, en_sci]

pl_points = 0
en_points = 0

def restart() :
      clear()
      game()

def clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')

def game():
      global pl_points
      global en_points

      print(title)

      print("INSTRUCTIONS : 1 = rock    2 = paper   3 = scissors", end='')
      print("")
      print("")
      print("")

      print(" You = ",pl_points,"                      Foe = ", en_points)
      print("")

      pl_move = input()

      try:
            pl_move = int(pl_move)-1
      except ValueError:
            restart()

      en_move = random.randint(0, 2)

      try :
            pl_print = pl_moves[pl_move]      
            en_print = en_moves[en_move]    
      except IndexError:
            restart()


      for i in range(6) :
                  print(pl_print[i], end = '')
                  print(en_print[i])

      victory = 0

      if en_move == pl_move :
            victory = 0
      if en_move == (pl_move+1)%3 :
            victory = -1
      if en_move == (pl_move+2)%3 :
            victory = 1

      print("")

      if victory == -1 :
            en_points += 1
            print("                 You lose")

      if victory == 0 :
            print("                 Tied")

      if victory == 1 :
            pl_points += 1
            print("                 You won!")
      
      print("")
      
            
      input("Press Enter to continue...")
      restart()
      

restart()