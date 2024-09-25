#Name:
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead
#has asked you to create a nested dictionary containing five enemy
#creatures (and their properties) for combat testing. Additionally,
#the testers are asking for a way to input changes to the enemy's
#damage values for balancing, as well as having it print those changes to
#confirm they went through.

#It is up to you to decide what properties
#are important and the theme of the game.

#UPDATE: The testers have run into some bugs with your code. Some of the
#code seems to not work correctly. For example, one of the testers changed
#the damage for an enemy to 30 per attack, but when they attacked the player
#character, the health went from 100 to 10030 instead of the intended 70.
#Your team lead has asked you to fix the bug.
#(HINT: The player's health is stored as an integer.)

#Make a nested dictionary containing 5 items

enemyDict = {
    "goblin" : {
        "Health" : 6,
        "Damage" : 2,
        "AC" : 12
    },
    "orc": {
        "Health" : 14,
        "Damage" : 6,
        "AC" : 14
    },
    "troll": {
        "Health" : 22,
        "Damage" : 10,
        "AC" : 13
    },
    "dragon": {
        "Health" : 56,
        "Damage" : 40,
        "AC" : 17
    },
    "mindflayer": {
        "Health" : 110,
        "Damage" : 55,
        "AC" : 16
    }
}

#Prompt User to change damage of each enemy in dictionary
enemyDict["goblin"]["Damage"] = int(input("Enter new damage value for Goblin: "))
enemyDict["orc"]["Damage"] = int(input("Enter new damage value for Orc: "))
enemyDict["troll"]["Damage"] = int(input("Enter new damage value for Troll: "))
enemyDict["dragon"]["Damage"] = int(input("Enter new damage value for Dragon: "))
enemyDict["mindflayer"]["Damage"] = int(input("Enter new damage value for Mindflayer: "))

#Print the results
print("The new damage for Goblin is:", enemyDict["goblin"]["Damage"])
print("The new damage for Orc is:", enemyDict["orc"]["Damage"])
print("The new damage for Troll is:", enemyDict["troll"]["Damage"])
print("The new damage for Dragon is:", enemyDict["dragon"]["Damage"])
print("The new damage for Mindflayer is:", enemyDict["mindflayer"]["Damage"])