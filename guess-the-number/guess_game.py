import random

number = random.randint(1,25)
chances = 0
flag=0

print("Guess a number between 1 and 25")

while(chances<5 and flag!=1):
    try:
        guess = int(input("Enter your guess:"))

        if guess==number:
            print("Congralution YOU WON!!!")
            flag=1
            exit()
        elif guess < number:
            print("Your guess was low. Try again :(")   
        else:
            print("Your guess was high. Try again :(")

        chances+=1
        print("Chances left : ",5-chances)
        
    except:
        if flag==1:
            exit()
        else:
            print("Invalid input! Enter again.")
    if chances==5:
        print("YOU LOSE!!! The number is : ",number)
