#!/usr/bin/env python3

'''
Description: Computer attempts to guess a number you choose between 1 and 1000 in 10 tries
Author: github.com/JeswinSunsi
'''

player_says = 'yes'
print('\n')
print ("Hi! I am Numinator, a Genie programmed in Python 3.8")

print('\n')
print("I want you to guess a number within 1-1000.")
print("I will try to guess your number within 10 tries.")
print('\n')


while player_says == "yes":
    tries_done = 10
    the_answer = 500
    lowest_num = 1
    highest_num = 1000
    while tries_done != 0:  
        try:
            print ("I think the answer is: ",the_answer)
            print ("")
            print ("Please type: 1 if my try is too high")
            print ("             2 if my try is too low")
            print ("             3 if I guessed your number")
            print ("")
            player_answer  = int (input("So did I guess right? "))
            print ("")
            if 1 < player_answer > 3:
                print ("Please enter a valid answer. 1, 2 and 3 are the valid choice")
                tries_done = tries_done + 1
            if player_answer == 1:
                highest_num = the_answer
                print ("Hmm, so your number is between ",lowest_num, "and ", highest_num)
                tries_done = tries_done - 1
                print (tries_done, "attempts left")
                the_answer = int (((highest_num - lowest_num)/2) + lowest_num)
                if the_answer <= lowest_num:
                    the_answer = the_answer + 1
                if highest_num - lowest_num == 2:
                    the_answer = lowest_num + 1
            elif player_answer == 2:
                lowest_num = the_answer
                print ("Hmm, so your number is between ",lowest_num, "and ", highest_num)
                tries_done = tries_done - 1
                print (tries_done, "attempts left")
                the_answer = int (((highest_num - lowest_num)/2) + lowest_num)
                if the_answer <= lowest_num:
                    the_answer = the_answer + 1
                if highest_num - lowest_num == 2:
                    the_answer = lowest_num + 1
            elif player_answer == 3:
                print ("Woo hoo! I won")
                tries_done = 0
        except:
            break
    else:
        player_says = input ('Like the app? Challenge me Again Yes/No ')

else:
    print ("Thank you for playing. Stay Awesome, keep Coding, and See you Again :)")
    print ("Contact the developers at jeswinsunsi@cyberdude.com")
