#Name:
#Class: 5th Hour
#Assignment: HW7

#1. Print Hello World!
print("Hello World!")
#2. Create three different boolean variables named wifi, login, and admin.
monke1 = True
monke2 = True
monke3 = True
#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
curiousGeorge = 8
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".

if monke1 == True:  #Create if statement that checks to see if monke1 is true.
    if monke2 == True: #Create nested if statement that checks to see if monke2 is true.
        if monke3 == True: #Create nested if statement that checks to see if monke3 is true.
            print("Welcome, Curious George!") #If ALL are true, print a welcome message
            curiousGeorge += 1 #increase the integer variable by one
            print(curiousGeorge)
        else: #If Monke3 is false
            print("Monke3 is not here!")
    else: #If Monke2 is false
        print("Monke2 is not here!")
else: #If Monke1 is false
    print("Monke1 is not here!")