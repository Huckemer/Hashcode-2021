from Light import Light
from Car import Car
from Intersection import Intersection
from Street import Street

def main():
    inputFile = open('C:/Users/colin/Documents/GitHub/Hashcode-2021/Qualification Round/a.txt',"r")

    lineCount = 0
    data = []
    cars = {}
    streets = {}
    intersections = {}
    incoming = {}
    idealPath = []
    currentState = {}

    for line in inputFile:
        data.append(line.split())

    temp = data.pop(0)
    # time duration
    d = int(temp[0])
    # number of intersections
    i = int(temp[1])
    # number of streets
    s = int(temp[2])
    # number of cars
    v = int(temp[3])
    # bonus points for each car that reaches its destination before d
    f = int(temp[4])

    # adding the streets
    while s > 0 and len(data) > 0:
        temp = data.pop(0)
        streets[temp[2]] = (Street(temp[0], temp[1], temp[2], temp[3]))
        s -= 1

    # adding the cars
    carCount = 0
    while v > 0 and len(data) > 0:
        temp = data.pop(0)
        tempCar = Car(carCount, temp[0], temp[1:], calculateCost(streets, temp[1:]))
        cars[carCount] = tempCar
        idealPath.append((carCount, tempCar.pathLength))
        streets[temp[1]].addCar(tempCar)
        v -= 1
        carCount += 1

    # adding the intersections
    for num in range(i):
        intersections[num] = Intersection(num)

    # filling in the intersections
    for street in streets:
        intersections[streets[street].end].addIncoming(streets[street])
        intersections[streets[street].start].addOutgoing(streets[street])

    # pairing the intersections
    for intersection in intersections:
        for street in intersections[intersection].incomingStreets:
            incoming[street.name] = intersection

    # set the current state
    for car in cars:
        currentIntersection = 0
        # print("car: " + str(car))
        for intersection in intersections:
            # print("intersection: " + str(intersection))
            # print("street: " + str(cars[car].streetNames[0]))
            for street in intersections[intersection].incomingStreets:
                if cars[car].streetNames[0] == street.name:
                    # print("found")
                    currentIntersection = intersection
                    break
        currentState[cars[car].number] = currentIntersection

    # optimize the car order
    idealPath.sort(key = lambda x: x[1])

    # print(d, i, s, v, f)
    # for intersection in intersections:
    #     intersections[intersection].print()
    # for street in streets:
    #     streets[street].print()
    print(incoming)
    print(idealPath)    
    # print(currentState)

    for time in range(d):
        moveCar(streets, cars[idealPath[0][0]], currentState, idealPath)
        print(currentState)


    outputFile = open("output.txt", "w")
    print("\n--------WRITING TO FILE---------")
    outputFile.write(str(len(intersections)))
    outputFile.close()
    print("--------DONE WRITING---------")

# calculate the route cost for the car
def calculateCost(streets, path):
    cost = 0
    for street in path:
        cost += streets[street].length
    return cost

def moveCar(streets, car, currentState, idealPath):
    oldStreet = car.streetNames[0]
    if len(car.streetNames) > 1:
        car.streetNames.pop(0)
        streets[car.streetNames[0]].addCar(car)
        # currentState[car.number] = 
        streets[oldStreet].cars.remove(car)
    else:
        streets[oldStreet].cars.remove(car)
        del currentState[car.number]
        del idealPath[car.number]


if __name__ == "__main__":
    main()