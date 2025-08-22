# create class
class Vehicle:

    # creare init method
    def __init__(self, max_speed, mileage):

        # bind the arguments
        self.max_speed = max_speed
        self.mileage = mileage

# object creation
model1 = Vehicle(240, 18)

# access the varriable inside init method
print("Model max speed : ",model1.max_speed)
print("Model mileage : ",model1.mileage)