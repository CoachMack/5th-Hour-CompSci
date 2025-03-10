#Name: Coach Mack
#Class: 5th Hour
#Assignment: Scenario 4

#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

players = int(input("Enter number of players: "))
i = 1
ratingSum = 0

if players < 2:
    print("Error, not enough players")
    exit()

while i <= players:
    rating = int(input("Enter rating from 1 to 5: "))
    if rating > 5 or rating < 1:
        print("Error, invalid rating.")
    else:
        ratingSum += rating
        i += 1

print("Average rating:", ratingSum / players)