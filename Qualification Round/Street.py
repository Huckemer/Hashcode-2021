class Street:

    def __init__(self, start, end, name, length):
        self.start = int(start)
        self.end = int(end)
        self.name = name
        self.length = int(length)
        self.cars = []
        self.light = 'R'

    def addCar(self, car):
        self.cars.append(car)

    def setGreen(self):
        self.light = 'G'
    
    def setRed(self):
        self.light = 'R'

    def print(self):
        print("Street: " + self.name)
        print("\tStart: " + str(self.start))
        print("\tEnd: " + str(self.end))
        print("\tLength: " + str(self.length))
        print("\tCar Count: " + str(len(self.cars)))
        print("\tCars: ")
        for car in self.cars:
            car.print()