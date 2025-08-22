# create attribute
class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

# instance the Parrot class
blu = Parrot("Blu", 10, "Black")
woo = Parrot("Woo", 15, "White")

# access the class attributes
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

# access the instance attributes
print("{} is {} years old and {} color".format(blu.name, blu.age, blu.color))
print("{} is {} years old and {} color".format(woo.name, woo.age, woo.color))