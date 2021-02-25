class Car:

    def __init__(self, number, pathLength, streetNames, routeCost):
        self.number = number
        self.pathLength = pathLength
        self.streetNames = streetNames
        self.routeCost = routeCost

    def print(self):
        print("\t\tCar Number: " + str(self.number))
        print("\t\tPath Length: " + str(self.pathLength))
        print("\t\tRoute Cost: " + str(self.routeCost))
        print("\t\tCar Start: " + self.streetNames[0])
        print("\t\tCar End: " + self.streetNames[-1] + "\n")