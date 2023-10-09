""" Rock Paper Scissors Game
    x is computer selection
    if x is 1 --> Rock, 2---> Paper 3 --> Scissors
    """

import random

print(""" Welcome to the GAME Rock paper Scissors
            and lets start the game""")

while True:
    choice = input("Enter your choice - Rock or Paper or Scissors (Press enter to quit)").capitalize()

    list = ['Rock', 'Paper', 'Scissors']

    a = random.choice(list)
    print(a)

    if choice == "":
        print("Stopping the Game. Good Bye!!!")
        break
    if (choice == 'Rock' and a == 'Rock') or (choice == "Rock" and a == "Rock"):
        print("Tie")
    if (choice == "Paper" and a== "Rock"):
        print("you win")
    if(choice == "Rock" and a =="Paper"):
        print("You loose")
    if(choice =="Scissors" and a=="Paper"):
        print("you win")
    if(choice =="Paper" and a =="Scissors"):
        print("you loose")
    if(choice == "Scissors" and a =="Paper"):
        print("you win")