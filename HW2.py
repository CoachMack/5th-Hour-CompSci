#Name: Coach Mack
#Class: 5th Hour
#Assignment: HW2

#Print Hello World!
print("Hello World!")
#Print a question asking for your name and a way for you to respond
name = input(print("What is your name? "))
nameTitle = name.title()
nameUpper = name.upper()
nameLower = name.lower()
print("Hello", name)
print("Hello", nameTitle)
print("Hello", nameUpper)
print("Hello", nameLower)

print(f"Hello to {name}'s 5th Hour Class")
#Have it ask for two integers from the user
x = int(input())
y = int(input())
#Add the two integers together and print them out
z = x + y
print(f"The Sum is: {z}")
