import time

print("-------------------- THE DRACONBAL ----------------------------\n")

for i in range(0, 6):
    time.sleep(i)

    print("Loading...")
    print(20*i ,"%")

    if i == 5:
        print("\n")

time.sleep(2)

print("""In a distant world named Hallo, a prosper (but agrresive)
race named draconytes lived until a horrible war devastate
their entire planet. The draconytes were capable to use their
vital life (named ogum) to increase the force of their hits.\n""")

time.sleep(2)

print("""During the war, all the planet of Hallo was destroyed, and
only two survived: Gaku and Vigetto. Their parents tryed to 
save them, so when they are babies, they were send to a little 
blue planet named Earth, and they are found by a farmer, and they 
lived 20 years in a farm.\n""")

time.sleep(1)

print("----------------------------------------------------------------")

time.sleep(1)

while True:

    p_choose = input("Now you can choose with who you will to play:\n -Gaku\n-Vigetto\n\n>")

    if p_choose == "Gaku":
        p_choose = 1
        break

    elif p_choose == "Vigetto":
        p_choose = 2
        break

    else:
        print("Sorry, i don't understand, please answer again.\n")
        continue

if p_choose == 1:
    
    life = 50
    power = 30
    xp = 0
    level = 1

    print(f"\nSTATUS:\n-LIFE: {life}\n-POWER: {power}\n-EXPERIENCE: {xp}\n LEVEL: {level}\n")

if p_choose == 2:
    
    life = 70
    power = 20
    xp = 0
    level = 1

    print(f"\nSTATUS:\n-LIFE: {life}\n-POWER: {power}\n-EXPERIENCE: {xp}\n LEVEL: {level}\n")

print("""You unfortunally die with COVID-19 because you didn't put a mask and 
didn't respect the quarentine, sorry :( !""")
