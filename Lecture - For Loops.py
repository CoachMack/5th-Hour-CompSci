#Name: Coach Mack
#Class: 5th Hour
#Assignment: Lecture - For Loops

import time
import random

#These are for loops. They work like while loops but have their own strengths and weaknesses.
x = random.randint(2,10)

print(x)
#The "range" function in a for loop goes from the first number to the number JUST BEFORE the
#second number. For this, you can do something like "x + 1" or add 1 to the number you intend
#as an easy workaround.
for i in range(1, x + 1):
    time.sleep(0.4)
    print(i)

#You can also add a third number to the "range" function to serve as the increment. 3 makes it go
#up by 3 each time, in this example.
for a in range(2, 20, 3):
    print(a)

#It can also count down by using negative numbers. Just make sure to have the big number go first!
for b in range(20, 0, -1):
    print(b)
else:
    print("Happy Birthday!")

#You can also use for loops to print the values inside of a list, including strings!
fruits = ["banana", "blueberry", "apple", "orange"]
for y in fruits:
    print(y)
    #Conditional statements work just fine inside of for loops in the same way they do in while loops.
    if y == "apple":
        break


#For loops can also spell out words if you make the "in" range just a single string.
for z in "Samuel":
    print(z)



#You can nest loops inside of each other to do multiple combinations of math or other functions.
#Get creative!
adj = ["filthy", "curious", "cute"]
animals = ["monkey", "snake", "dog"]

for c in adj:
    for d in animals:
        print(c, d)

#You can put the "pass" function in an empty loop just to make the error go away while you're still working on it.
for h in []:
    pass
