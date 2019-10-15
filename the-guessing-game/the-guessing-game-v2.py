import random
n = random.randint(1, 99)
guess = -1
n_guesses = 0
while n != guess:
    print
    try:
        guess = int(input("Enter an integer from 1 to 99: "))
        if guess < 1 or guess > 99:
            print("guess should be in the range from 1 to 99!")
        elif guess < n:
            n_guesses += 1
            print("guess is low")
        elif guess > n:
            n_guesses += 1
            print("guess is high")
        else:
            n_guesses += 1
            print(f"you guessed it in {n_guesses} guesses!\ncan you do better in the next time?")

    except:
        print("guess is in an incorrect format! (expected an integer between 1 and 99)")
    print
