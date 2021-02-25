class Street:

    def __init__(self, start, end, name, length):
        self.start = int(start)
        self.end = int(end)
        self.name = name
        self.length = int(length)
        self.cars = []

    def addCar(self, car):
        self.cars.append(car)

    def print(self):
        print("Street: " + self.name)
        print("\tStart: " + str(self.start))
        print("\tEnd: " + str(self.end))
        print("\tLength: " + str(self.length))
        print("\tCar Count: " + str(len(self.cars)))
        print("\tCars: ")
        for car in self.cars:
            car.print()