class Car(object):
    wheels = 4

    def __init__(self, make):
        self.make = make

newCar = Car("Honda")
print ("My new car is a {}".format(newCar.make))
print ("My car, like all cars, has {} wheels".format(Car.wheels))

