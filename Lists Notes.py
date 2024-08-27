
santasList = ["Sam", "Gage", "Quinn", "Ethan", "Preston", "Eric", "Chaysen", "Kevin", "Gabriel", "Dominic", "Zachary", "Ryley", "Eli", "The Other Ethan"]
santasList.insert(3, input())
print(santasList[10])
santasList.remove("Dominic")
print(santasList[10])
#print(f"{santasList[0]} is NAUGHTY!")
#print(f"{santasList[1]} is NAUGHTY!")
#print(f"{santasList[8]} is NAUGHTY!")
print(f"{santasList[3]} is NAUGHTY!")
print()

numberList = [5, 2, 6, 6]
numberList.sort(reverse=True)
print(numberList)
numberList.append(5)
sum = numberList[0]+numberList[1]+numberList[2]+numberList[3]
print(sum)
sumAppend = sum + numberList[4]
print(sumAppend)

mixList = ["Tommy", True, 7]
print(mixList)
