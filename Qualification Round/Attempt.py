from Light import Light
from Car import Car
from Intersection import Intersection
from Street import Street

def main():
    # open the input file for reading
    inputFile = open('C:/Users/colin/Documents/GitHub/Hashcode-2021/Qualification Round/a.txt',"r")

    # extract the data from the input file
    data = []
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

    # the ideal order to send the cars in
    idealOrder = []
    # the current locations of the cars
    currentState = {}

    # cars waiting at the lights. number: Car Object
    waiting = {}
    # cars driving on the streets and how far they have to go. number: Car Object
    driving = {}
    # log of lights switched to green and when. streetName: [(time changed, color, intersection)]
    log = {}

    # the intersections/nodes. number: Intersection Object
    intersections = {}
    # the streets/edges between intersections/nodes. streetName: (start, end, Street Object)
    streets = {}
    # the cars traveling in the city/graph. number: Car Object
    cars = {}

    # adding the streets/edges
    while s > 0 and len(data) > 0:
        temp = data.pop(0)
        streets[temp[2]] = (int(temp[0]), int(temp[1]), Street(temp[0], temp[1], temp[2], temp[3]))
        s -= 1

    # adding the cars
    carCount = 0
    while v > 0 and len(data) > 0:
        temp = data.pop(0)
        tempCar = Car(carCount, temp[0], temp[1:], calculateCost(streets, temp[1:]))
        cars[carCount] = tempCar
        waiting[carCount] = tempCar
        idealOrder.append((carCount, tempCar.pathLength))
        v -= 1
        carCount += 1

    # adding the intersections/nodes
    for num in range(i):
        intersections[num] = Intersection(num)

    # fill in which streets are possible lights
    for street in streets:
        intersections[streets[street][2].end].addIncoming(streets[street][2].name)

    # optimize the car order
    idealOrder.sort(key = lambda x: x[1])

    # PRINT STATEMENTS
    print(d, i, s, v, f)
    print("Waiting:")
    print(waiting)
    print("Driving:")
    print(driving)
    # for intersection in intersections:
    #     intersections[intersection].print()
    print("Ideal Order:")
    print(idealOrder)    

    # SIMULATION
    for currentTime in range(d):
        # if the most ideal car is waiting, change the light to green
        if idealOrder[0][0] in waiting:
            car = waiting[idealOrder[0][0]]
            # if the intersection already has a green light, change that to red
            for incomingStreet in intersections[streets[car.streetNames[0]][1]].incomingStreets:
                if streets[incomingStreet][2].light == 'G':
                    streets[incomingStreet][2].setRed()
            print("Car: " + str(car.number) + " let through intersection: " + str(streets[car.streetNames[0]][1]))
            # change the light to green
            streets[car.streetNames[0]][2].setGreen()
            # change the car's current location
            car.streetNames.pop(0)
            # when the car goes through the light, change it to driving
            driving[idealOrder[0][0]] = waiting[idealOrder[0][0]]
            del waiting[idealOrder[0][0]]
            # set the driving car's arrival time
            car.setArrivalTime(currentTime + streets[car.streetNames[0]][2].length)

        # if the most ideal car is driving, check the next most ideal to see if it's waiting
        else:
            for pair in idealOrder:
                if pair[0] in waiting:
                    car = waiting[pair[0]]
                    # if the intersection already has a green light, change that to red
                    for incomingStreet in intersections[streets[car.streetNames[0]][1]].incomingStreets:
                        if streets[incomingStreet][2].light == 'G':
                            streets[incomingStreet][2].setRed()
                    print("Car: " + str(car.number) + " let through intersection: " + str(streets[car.streetNames[0]][1]))
                    # change the light to green
                    streets[car.streetNames[0]][2].setGreen()
                    # change the car's current location
                    car.streetNames.pop(0)
                    # when the car goes through the light, change it to driving
                    driving[pair[0]] = waiting[pair[0]]
                    del waiting[pair[0]]
                    # set the driving car's arrival time
                    car.setArrivalTime(currentTime + streets[car.streetNames[0]][2].length)

        # if any cars are driving on their destination street, remove them
        # if a driving car's arrival time is the current time, move them to waiting for their light
        finished = []
        for car in driving:
            if len(driving[car].streetNames) == 1:
                finished.append(car)
            elif driving[car].arrivalTime == currentTime:
                waiting[car] = driving[car]
                finished.append(0)
        for car in finished:
            del driving[car]
        

    # write the log to the file in the correct format
    outputFile = open("output.txt", "w")
    print("\n--------WRITING TO FILE---------")
    # amount of intersections with schedules
    scheduledIntersections = 0
    # all intersections on schedule
    finalIntersections = []
    for intersection in intersections:
        for street in intersections[intersection].incomingStreets:
            if streets[street][2].name in log:
                scheduledIntersections += 1
                finalIntersections.append([intersection, streets[street][2].name, log[streets[street][2].name][0][1] - log[streets[street][2].name][0][0]])
    outputFile.write(str(scheduledIntersections))
    # sort the entries chronologically
    finalIntersections.sort(key = lambda x: x[2])
    # for all intersections on schedule
    for entry in finalIntersections:
        # intersection on schedule

        # amount of lights changed in intersection
        
        # names of streets changed in order, and for how long
        
        pass

    print("...")
    outputFile.close()
    print("----------DONE WRITING----------")

# calculate the total intended path length for the car
def calculateCost(streets, path):
    cost = 0
    for street in path:
        cost += streets[street][2].length
    return cost

if __name__ == "__main__":
    main()