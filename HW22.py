#Name: Coach Mack
#Class: 5th Hour
#Assignment: HW22

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class StoreItems:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight

    def double_cost(self):
        self.cost *= 2

#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
apple = StoreItems(60, 0.25, 0.5)
banana = StoreItems(50, 0.17, 0.25)
orange = StoreItems(100, 0.14, 0.20)
#3. Print the stock of all three objects and the cost of the second store item.
print("Stock of Apples:", apple.stock)
print(f"Stock of Bananas: {banana.stock}")
print("Stock of Oranges:", orange.stock)

print(f"Cost of Bananas: {banana.cost}")
#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
banana.double_cost()
print(f"New Cost of Bananas: {banana.cost}")
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
orange.stock = 25
print("New Stock of Oranges:", orange.stock)
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del apple

try:
    print(apple.weight)
except NameError:
    print("Item Out of Stock")