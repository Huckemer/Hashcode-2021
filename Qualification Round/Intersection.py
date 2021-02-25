from Light import Light

class Intersection:

    def __init__(self, number):
        self.number = int(number)
        self.incomingStreets = []
        self.outgoingStreets = []

    def addIncoming(self, street):
        self.incomingStreets.append(street)

    def addOutgoing(self, street):
        self.outgoingStreets.append(street)

    def print(self):
        print("\nIntersection Number: " + str(self.number))
        print("Incoming Streets: ")
        for street in self.incomingStreets:
            print(street.name)
        print("Outgoing Streets: ")
        for street in self.outgoingStreets:
            print(street.name)
    