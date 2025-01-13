#Name: Coach Mack
#Class: 5th Hour
#Assignment: Lecture - Def Functions
import random

def hello_world():
    print("Hello World!")

hello_world()

def class_roster(name):
    print(name, "is in 5th hour.")

class_roster("Kevin")

def subtraction(a, b):
    print(a - b)

subtraction(b = 15, a = 27)

def student_name(**student):
    print("This student's last name is " + student["lname"])

student_name(fname = "Dom", lname = "Acuna", grade = "Senior", vidya = "CoD")

def number_game():
    playerNum = int(input("Enter number between 1 and 10"))
    opponentNum = random.randint(1, 10)

    print(f"Opponent got {opponentNum}")
    if playerNum > opponentNum:
        print("You win!")
    elif opponentNum > playerNum:
        print("Opponent Win!")
    else:
        print("Tie!")

    replayInput = input("Would you like to play again? Y/N ")

    if replayInput == "Y":
        number_game()
    else:
        exit()

number_game()