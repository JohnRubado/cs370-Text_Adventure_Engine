from packages.area.area import Area
from packages.transition.transition import transition;
from packages.player.player import player;

class world:
    NORTH = 0;
    EAST = 1;
    SOUTH = 2;
    WEST = 3;
    player = player("Player One");

    def __init__(self,name = "A brand new world!", playerName = "Player"):
        self.name = name;
        self.playerName = playerName;
        self.areas = [];



    #function verifies valid cardinal direction.
    def validCardinalDirection(self, cardinalPosition):
        validCardinalDir = False;
        cardinalPosition = cardinalPosition.lower();
        if cardinalPosition == "east":
            validCardinalDir = True;
        elif cardinalPosition == "west":
            validCardinalDir = True;
        elif cardinalPosition == "north":
            validCardinalDir = True;
        elif cardinalPosition == "south":
            validCardinalDir = True;
        return validCardinalDir;

    #function searches for existence of an area, returns true if found and false if not found
    def areaExists(self, area):
        areaFound = False;
        for possibleArea in self.areas:
            if possibleArea.name == area:
                areaFound = True;
        return areaFound;

    def setStart(self, areaName):
        areaFound = self.areaExists(areaName);
        if areaFound:
            self.player.currentArea = areaName;
        else:
            raise Exception("Area named " + areaName + "does not exist");

#SOOOO, This gets a little confusing. But basically we search to find what area the player is in so we can access that area object itself (coulda been done better prolly).
#Then we determine if the direction they want to go has a transition objectself.
#If it does, we move the player to the destination that the transition object leads to.
## TODO: Make it so that we display a message if what the user typed is not an available action for that transition
    def movePlayer(self,cardinalDirection):

        playerMoved = False;
        destination = "";
        player = self.player;
        if self.validCardinalDirection(cardinalDirection):
            for area in self.areas:
                if player.currentArea == area.name and playerMoved == False:
                    if cardinalDirection == "north":
                        if area.directions[self.NORTH].transition != None:
                            destination = area.directions[self.NORTH].transition.destination;
                            player.currentArea = destination;
                            print player.name + " has taken the " + area.directions[self.NORTH].transition.name + " in the " + cardinalDirection;
                            playerMoved = True;
                        else:
                            print "There is no route that leads " + cardinalDirection;
                    elif cardinalDirection == "east":
                        if area.directions[self.EAST].transition != None:
                            destination = area.directions[self.EAST].transition.destination;
                            player.currentArea = destination;
                            print player.name + " has taken the " + area.directions[self.EAST].transition.name + " in the " + cardinalDirection;
                            playerMoved = True;
                        else:
                            print "There is no route that leads " + cardinalDirection;
                    elif cardinalDirection == "south":
                        if area.directions[self.SOUTH].transition != None:
                            destination = area.directions[self.SOUTH].transition.destination;
                            player.currentArea = destination;
                            print player.name + " has taken the " + area.directions[self.SOUTH].transition.name + " in the " + cardinalDirection;
                            playerMoved = True;
                        else:
                            print "There is no route that leads " + cardinalDirection;
                    else:
                        if area.directions[self.WEST].transition != None:
                            destination = area.directions[self.WEST].transition.destination;
                            player.currentArea = destination;
                            print player.name + " has taken the " + area.directions[self.WEST].transition.name + " in the " + cardinalDirection;
                            playerMoved = True;
                        else:
                            print "There is no route that leads " + cardinalDirection;

        else:
            print "What is " +cardinalDirection + "? there is no " + cardinalDirection;
        #This ethod takes an array of descriptions with an array of cardinalDirections of where to put those descriptions.
        #dont forget to check for existence of the areaName
    def setAreaDescriptions(self,areaName,descriptions, cardinalDirections):
        print "";


    def newArea(self,name):
        for area in self.areas:
            if area.name == name:
                raise Exception("Area named " + name + " already exists");
        newArea = Area(name);
        self.areas.append(newArea);

        #if this is the first area made then the players position defaults to it
        if len(self.areas) == 1:
            self.setStart(self.areas[0].name);

    def printWorld(self):

        print "World: " + self.name;
        print "\tAreas:";
        for area in self.areas:
            print "\t" + area.name + " containing transitions: "
            for direction in area.directions:
                if direction.transition != None:
                    print "\t\t" + direction.transition.name + " in the " + direction.direction;
        print "player named " + self.player.name + " is at " + self.player.currentArea;

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

        if areaFound == False:
            raise Exception("Area " + area + " does not exist");

        #checking for existence of target destination
        for possibleDest in self.areas:
            if possibleDest.name == destination:
                destinationFound = True;
                targetDestination = possibleDest.name;

        if destinationFound == False:
            raise Exception("Destination " + destination + " does not exist");
        cardinalPosition = cardinalPosition.lower();

        #checking if cardinalPosition is valid
        if  self.validCardinalDirection(cardinalPosition) == False:
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

            if cardinalPosition == "east":
                self.newTransition(name, destination, area, "west", possibleActions, False);
            elif cardinalPosition == "west":
                self.newTransition(name, destination, area, "east",possibleActions, False);
            elif cardinalPosition == "north":
                self.newTransition(name, destination, area, "south", possibleActions, False);
            elif cardinalPosition == "south":
                self.newTransition(name, destination, area, "north", possibleActions, False);
