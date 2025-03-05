#Name: Coach Mack
#Class: 5th Hour
#Assignment: Lecture - Classes and Objects

#This is a class. These are used to apply certain attributes to a specific variable, known as an object.
#Python is what is called an "object-oriented" language. It is about taking things and doing things
#with those things. More practical than conceptual.
class Character:
    #Inside a class, you initialize it with an __init__ function, and assign to a variable called "self".
    #Self is the placeholder for objects so it can assign those specific attributes when the class is used.
    def __init__(self, health, damage, ammo):
        self.health = health
        self.damage = damage
        self.ammo = ammo

    #You can put functions inside of a class that allows you to use the functions to specific objects when called.
    def one_third_damage_nerf(self):
        self.damage *= (2/3)
    def health_10_percent_buff(self):
        self.health *= (11/10)

#This is an object. By assigning a class to a variable, the numbers inside represent the object's
#attributes. In this case, wrecking ball has 675 health, 25 damage, and 100 ammo.
wreckingball = Character(675, 25, 100)
genji = Character(250, 30, 30)

print(f"Wrecking Ball DPS: {wreckingball.damage}")
print(f"Genji DPS: {genji.damage}")

#You can use functions inside of a class to change the attributes to an object at will without having
#to change the original values or repeat the code for multiple objects.
genji.one_third_damage_nerf()
wreckingball.health_10_percent_buff()
print(f"Genji New DPS: {genji.damage}")
print(f"Wrecking Ball New Health: {wreckingball.health}")

#You can also change the attribute directly if you need to and it will apply.
wreckingball.health = 700
print(f"Wrecking Ball New Health (should be at 700): {wreckingball.health}")

#You can also delete objects if an object needs to be deleted for whatever reason.
del genji

#Just like if functions and def functions, classes can't be left empty so you can add
#pass to prevent errors.
class NPC:
    pass



