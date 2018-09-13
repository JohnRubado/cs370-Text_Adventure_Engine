from packages.area.area import Area
from packages.transition.transition import transition;

class world:

    areas = None;
    name = "";

    def __init__(self,name):
        self.name = name;
        self.areas = [];

    def newArea(self,name):
        for area in self.areas:
            if area.name == name:
                raise Exception("Area named " + name + " already exists");
        newArea = Area(name);
        self.areas.append(newArea);

    def printWorld(self):

        print "World: " + self.name;
        print "\tAreas:";
        for area in self.areas:
            print "\t" + area.name + " containing transitions: "
            for direction in area.directions:
                if direction.transition != None:
                    print "\t\t" + direction.transition.name + " in the " + direction.direction;

    def newTransition(self, name, area, destination, cardinalPosition, possibleActions, isTwoWay):

        areaFound = False;
        destinationFound = False;
        validCardinalPosition = False;
        targetArea = None;
        targetDestination = None;

        #ERROR CHECKING UP FRONT
            #checking for existence of target area
        for possibleArea in self.areas:
            if possibleArea.name == area:
                areaFound = True;
                targetArea = possibleArea;
                #print targetArea.name;

        if areaFound == False:
            raise Exception("Area " + area + " does not exist");

        #checking for existence of target destination
        for possibleDest in self.areas:
            if possibleDest.name == destination:
                destinationFound = True;
                targetDestination = possibleDest;

        if destinationFound == False:
            raise Exception("Destination " + destination + " does not exist");

        #checking if cardinalPosition is valid
        if cardinalPosition.lower() == "east":
            validCardinalPosition = True;
        elif cardinalPosition.lower() == "west":
            validCardinalPosition = True;
        elif cardinalPosition.lower() == "north":
            validCardinalPosition = True;
        elif cardinalPosition.lower() == "south":
            validCardinalPosition = True;
        else:
            raise Exception("Cardinal position " + cardinalPosition + " is an invalid cardinal position ");

            #this logic here is recursive. If the transition is one way then we simply create the transition and place it in the area.
            #if it is two way, we
        if isTwoWay == False:
            newTransition = transition(name, targetArea, targetDestination, cardinalPosition, possibleActions);
            targetArea.newTransition(newTransition);
        if isTwoWay == True:
            newTransition = transition(name, targetArea, targetDestination, cardinalPosition, possibleActions);
            targetArea.newTransition(newTransition);
            #Swap destination with area, invert cardinalPosition, invert isTwoWay because we are putting the transition in the other room
            if cardinalPosition.lower() == "east":
                self.newTransition(name, destination, area, "west", possibleActions, False);
            elif cardinalPosition.lower() == "west":
                self.newTransition(name, destination, area, "east",possibleActions, False);
            elif cardinalPosition.lower() == "north":
                self.newTransition(name, destination, area, "south", possibleActions, False);
            elif cardinalPosition.lower() == "south":
                self.newTransition(name, destination, area, "north", possibleActions, False);
