#Name: Coach Mack
#Class: 5th Hour
#Assignment: Lecture - Refresher

import random

x = random.randint(1,5)
y = random.randint(1,100)
z = 0
numList = [3, 8, 32, 77]

if x == 1:
    print("X is 1")
elif x == 2:
    print("X is 2")
elif x == 3:
    print("X is 3")
elif x == 4:
    print("X is 4")
else:
    print("X is 5")

print(y)
if y > 20 and y < 80:
    print("Grade is greater than 20 but less than 80")
elif y <= 20:
    print("Grade is less than or equal to 20")
elif y >= 80:
    print("Grade is greater than or equal to 80")


while z < 5:
    z += 1
    print(z)

for i in range(1, 6):
    print(i)

for j in numList:
    print(j)

lower = 2
upper = 1000
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

