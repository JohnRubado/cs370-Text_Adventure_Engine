from packages.area.area import Area
from packages.transition.transition import transition;
from packages.player.player import player;
from packages.item.item import item;

#TODO: Add functionality for looking in  direction

class world:
    NORTH = 0;
    EAST = 1;
    SOUTH = 2;
    WEST = 3;


    #AUTHOR METHODS
    def __init__(self,name = "A brand new world!", playerName = "Player One"):
        self.name = name;
        self.player = player(playerName);
        self.areas = [];
    def setStart(self, areaName):
        areaFound = self.areaExists(areaName);
        if areaFound:
            self.player.currentArea = areaName;
        else:
            raise Exception("Area named " + areaName + "does not exist");
    def newArea(self,name, description):
        for area in self.areas:
            if area.name == name:
                raise Exception("Area named " + name + " already exists");
        newArea = Area(name,description);
        self.areas.append(newArea);

        #if this is the first area made then the players position defaults to it
        if len(self.areas) == 1:
            self.setStart(self.areas[0].name);


    #PARSER METHODS
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
                                print "You have taken the " + area.directions[self.NORTH].transition.name + " in the " + cardinalDirection;
                                playerMoved = True;
                            else:
                                print "There is no route that leads " + cardinalDirection;
                        elif cardinalDirection == "east":
                            if area.directions[self.EAST].transition != None:
                                destination = area.directions[self.EAST].transition.destination;
                                player.currentArea = destination;
                                print "You have taken the " + area.directions[self.EAST].transition.name + " in the " + cardinalDirection;
                                playerMoved = True;
                            else:
                                print "There is no route that leads " + cardinalDirection;
                        elif cardinalDirection == "south":
                            if area.directions[self.SOUTH].transition != None:
                                destination = area.directions[self.SOUTH].transition.destination;
                                player.currentArea = destination;
                                print "You have taken the " + area.directions[self.SOUTH].transition.name + " in the " + cardinalDirection;
                                playerMoved = True;
                            else:
                                print "There is no route that leads " + cardinalDirection;
                        else:
                            if area.directions[self.WEST].transition != None:
                                destination = area.directions[self.WEST].transition.destination;
                                player.currentArea = destination;
                                print"You have taken the " + area.directions[self.WEST].transition.name + " in the " + cardinalDirection;
                                playerMoved = True;
                            else:
                                print "There is no route that leads " + cardinalDirection;

            else:
                print "What is " +cardinalDirection + "? there is no " + cardinalDirection;

            if playerMoved == True:
                self.look();
            #This ethod takes an array of descriptions with an array of cardinalDirections of where to put those descriptions.
            #dont forget to check for existence of the areaName
    def look(self, target = ""):

        playerArea = self.player.currentArea;#string
        validCardinalDirection = self.validCardinalDirection(target);
        currAreaIndex = self.getArea(playerArea);
        areaObj = self.areas[currAreaIndex]#obj
        if target == "":
            print "It appears I am in a " + areaObj.name + ". " + areaObj.description;
            print "I see "
            for item in areaObj.items:
                print item.name + " "+ item.description
            for direction in areaObj.directions:
                if direction.transition != None:
                    print "I see a " + direction.transition.name + " in the " + direction.direction;
        elif validCardinalDirection == True:
            #just a direction
            print "looking " + cardinalDirection;

    #HELPER METHODS
    #calling of this function may throw an exception if
    #the area does not exist.
    def getArea(self, areaName):

        if self.areaExists(areaName):
            for possibleArea in self.areas:
                if possibleArea.name == areaName:
                    return self.areas.index(possibleArea);
        else:
            raise Exception("Area named " + areaName + "does not exist");
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

    def setAreaDescriptions(self,areaName,descriptions, cardinalDirections):
        print "";

    def newItem(self,name,description,areaName):
        targetArea=self.areas[self.getArea(areaName)]
        newitem=item(name,description)
        targetArea.newItem(newitem)




    def printWorld(self):

        print "World: " + self.name;
        print "\tAreas:";
        for area in self.areas:
            print "\t" + area.name + " containing transitions: "
            for direction in area.directions:
                if direction.transition != None:
                    print "\t\t" + direction.transition.name + " in the " + direction.direction;
        print "player named " + self.player.name + " is at " + self.player.currentArea;
