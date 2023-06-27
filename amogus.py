from os import system
from time import sleep
from random import choice, randint


identification = []
identity_running = True

print("Welcome to Amogus, where you can play Among Us in school\n\nPress Enter to continue")
input("")  # Wait for user to press enter

system("cls") # Clear the shell

while identity_running:
    name = input("Enter your alias: ")
    birthdate = input("Enter your birthdate: ")
    origin = input("Enter your origin: ")
    identification.append(name)
    identification.append(birthdate)
    identification.append(origin)

    system("cls")

    sleep(0.46)
    print("Forging ID")
    sleep(1.32)
    print("Forging Documents")
    sleep(1.74)

    system("cls")

    print(f"IDENTIFICATION\n-------------------------------------------------\nName: {name}\nBirthdate: {birthdate}\nOrigin: {origin}\n")
    approved = input("(Y/N) ")
    if len(approved) == 1 and approved == "Y":
        identity_running = False
    else:
        print("Try again. The officers denied you access. Press Enter to continue")
        input("")
        continue

won = False
crewmates = 8
round = 1
colors = ["Red" ,"Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Brown"]

system("cls")
print("The officers have granted you access to the ship. Your job is to sabotage the ship and murder all of the crewmates aboard.\n\nThe game is about to begin.")
sleep(0.87)
system("cls")

while crewmates > 1 and not won:
    who_to_kill = choice(colors)
    kill_number = randint(1, 20)
    print(f"This is round {round}. You are asked to kill {who_to_kill}. If you fail to kill {who_to_kill}, you will automatically lose the game.")
    if kill_number > 0 and kill_number < 5:
        print(f"\nUsing your expertise, {who_to_kill} has been expertly assassinated with a swift neck break. {who_to_kill} is successfully out of the game.")
    colors.remove(who_to_kill)
    crewmates -= 1
