from os import system
from time import sleep
from random import choice, randint


identification = []
identity_running = True

print("Welcome to Amogus, where you can play Among Us in school!\n\nPress Enter to continue")
input("")  # Wait for user to press enter

system("cls") # Clear the shell

while identity_running:
    system("cls")
    name = input("Enter your alias: ")
    birthdate = input("Enter your birthdate: ")
    origin = input("Enter your origin: ")
    identification.append(name)
    identification.append(birthdate)
    identification.append(origin)

    system("cls")

    sleep(0.46)
    print("Forging Fake ID")
    sleep(1.32)
    print("Forging Fake Documents")
    sleep(1.74)

    system("cls")

    print(f"IDENTIFICATION\n-------------------------------------------------\nName: {name}\nBirthdate: {birthdate}\nOrigin: {origin}\n")
    approved = input("(Y/N) ")
    if len(approved) == 1 and approved.lower() == "y":
        identity_running = False
    else:
        print("Try again. The officers denied you access and if they find you again then you will be taken prisoner by the FBI. Press Enter to continue")
        input("")
        continue

status = 0
round_ = 1
colors = ["Red" ,"Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Brown"]

system("cls")
print("The officers have granted you access to the space ship. Your job is to sabotage the ship and murder all of the crewmates aboard to steal all their money and take it to your boss who is the leader of the Russian Mafia or else you will die.\n\nThe game is about to begin.")
sleep(2.19)
system("cls")

while round_ < 8 and status == 0:
    who_to_kill = choice(colors)
    kill_number = randint(1, 20)
    print(f"This is round {round_}. You are asked to kill {who_to_kill}. If you fail to kill {who_to_kill}, you will automatically lose the game because they killed you and took the money for themselves.")
    print("\nPress Enter to continue")
    input("")
    system("cls")
    attack_roll = randint(1, 10)
    hidden_roll = randint(1, 10)
    redemption_roll = randint(1, 5)
    persuasion_roll = randint(1, 10)
    print(f"Attack: {attack_roll}\nHidden: {hidden_roll}\n--------------------------------------------------------")
    if attack_roll > 2:
        print(f"The target {who_to_kill} was succesfully terminated by you...")
        colors.remove(who_to_kill)
        sleep(5)
    else:
        print(f"The target {who_to_kill} escaped your wrath. You have one more chance to kill them...")
        sleep(5)
        system("cls")
        print(f"Redemption: {redemption_roll}\n--------------------------------------------------------\n")
        hidden_roll -= 3
        if redemption_roll < 4:
            print("You failed to kill the target, and you have been reported to the FBI and ejected. Have a good life!")
            sleep(5)
            status = -1
        else:
            print("The target was succesfully eliminated, but your persuasion techniques have become a lot more dull. Have fun at the meeting...")
            colors.remove(who_to_kill)
            hidden_roll -= 3
            sleep(5)

    system("cls")
    colors_nice = '\n'.join(colors)
    if status == 0 and len(colors) != 1:
        print(f"MEETING\n----------------------------------------------------\nPlayers Alive:\n{colors_nice}\n")
        if hidden_roll < 2:
            print("You have been backstabbed by one of the crewmates, and you have been ejected. Enjoy the afterlife...")
            status = -1
            sleep(3)
        elif hidden_roll < 4:
            print("You have been accused by many of the crewmates...")
            sleep(3)
            if persuasion_roll > 5:
                print("Luckly, you have convinced them that you are a crewmate. This might not work next time...")
                sleep(3)
            else:
                print("Your luck ran out this time, and the crewmates discovered you were the impostor. Better luck next time!")
                status = -1
                sleep(3)
        else:
            print("You were accused by only one person...\nThis time you got lucky, just don't get cocky...")
            sleep(3)

    system("cls")
        
    try:
        round_ += 1
        colors.remove(who_to_kill)
    except Exception:
        pass

system("cls")

if status < 0:
    print("\"YOU FAILURE. I WILL MELT YOUR LITTLE BRAIN IN HALF.\"\n    - BOSS")
else:
    print("Congratulations, you succesfully have eliminated the entire crew and successfully have retrieved all of da money. Good job!")

while True:
    pass
