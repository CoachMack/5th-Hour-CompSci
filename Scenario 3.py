#Name:
#Class: 5th Hour
#Assignment: Scenario 3
import random

#Scenario 3:
#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.

#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).

#To make things easier, here is a reference list for party damage rolls.
#(Feel free to use similar numbers for your enemy dictionary.)

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4

#Step 1: Copy enemy dictionary from SC1

#Step 2: Copy party dictionary from SC2

#Step 3: Make sure every enemy and party member has health points (fixed)

#Step 4: Make sure every enemy and party member has an attack modifier (fixed)

#Step 5: Make sure every enemy and party member has an armor class (AC) (fixed)

#Step 6: Make every enemy and party member has a damage roll (random)

#Party Dictionary Goes Here
partyDict = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "AtkMod": 5,
        "Damage" : random.randint(1,6) + random.randint(1,6) + 3
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "AtkMod": 3,
        "Damage" : random.randint(1,6) + 3,
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "AtkMod": 5,
        "Damage" : random.randint(1,10),
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "AtkMod": 5,
        "Damage" : random.randint(1,6) + 4,
    }
}


#Enemy Dictionary Goes Here
enemyDict = {
    "Goblin" : {
        "Health" : 6,
        "AC" : 12,
        "AtkMod": 5,
        "Damage" : random.randint(1,6) + 4,
    },
    "Orc": {
        "Health" : 14,
        "AC" : 14,
        "AtkMod": 5,
        "Damage" : random.randint(1,6) + 4,
    },
    "Troll": {
        "Health" : 22,
        "AC" : 13,
        "AtkMod": 5,
        "Damage" : random.randint(1,6) + 4,
    },
    "Dragon": {
        "Health" : 56,
        "AC" : 17,
        "AtkMod": 5,
        "Damage" : random.randint(1,6) + 4,
    },
    "Mindflayer": {
        "Health" : 110,
        "AC" : 16,
        "AtkMod": 5,
        "Damage" : random.randint(1,6) + 4,
    }
}


#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#Step 7: Pick a party member

#Step 8: Pick an ememy

#Step 9: Create an attack roll for party member

#Step 10: Compare the party member attack roll to the enemy AC

#Step 11: Subtract damage from enemy health if it hits

#Step 12: Check to see if enemy is still alive

#Step 13: Step 9 through 12, but enemy attacks party member if still alive


#Combat Code Goes Here

#What do we need?
#- Enemy AC
#- Party Attack Mod
#- a D20 Roll
#- Enemy HP
#- Party Damage

#Party Member: Astarion
#Enemy: Goblin

#if attack roll is greater than or equal to enemy AC, we hit
if random.randint(1,20) + partyDict["Astarion"]["AtkMod"] >= enemyDict["Goblin"]["AC"]:
    #if we hit, subtract Party Damage from Enemy HP
    enemyDict["Goblin"]["Health"] -= partyDict["Astarion"]["Damage"]
#   if enemy HP is less than or equal to zero, end code
    if enemyDict["Goblin"]["Health"] > 0:
    #   else say that enemy is still alive, go to enemy turn
        print("Astarion hit! Gobbo is still alive!")
    else:
        print("Astarion hit! Gobbo is dead!")
        exit()
# if we miss, skip to enemy turn
else:
    print("Astarion missed!")


if random.randint(1,20) + enemyDict["Goblin"]["AtkMod"] >= partyDict["Astarion"]["AC"]:
    partyDict["Astarion"]["Health"] -= enemyDict["Goblin"]["Damage"]
    if partyDict["Astarion"]["Health"] <= 0:
        print("Gobbo hit! Astarion is down!")
        exit()
    else:
        print("Gobbo hit! Astarion is alive!")
else:
    print("No one hit!")