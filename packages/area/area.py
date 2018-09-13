from packages.item import item;
from packages.direction.direction import direction;
from enum import Enum;

class Area:

    transitions = None;
    items = [];
    directions = None;
    north = None;
    east = None;
    south = None;
    west = None;

    def __init__(self,name):
        self.name = name;
        self.north = direction("north");
        self.east = direction("east");
        self.south = direction("south");
        self.west = direction("west");
        self.directions = [None,None,None,None];
        self.directions[0] = self.north;
        self.directions[1] = self.east;
        self.directions[2] = self.south;
        self.directions[3] = self.west;

    def newItem(self, item):
        print "TBD";

    def newTransition(self, transition):
        cardinalPosition = transition.cardinalPosition;

        if cardinalPosition == "north":
            self.north.newTransition(transition);
        elif cardinalPosition == "east":
            self.east.newTransition(transition);
        elif cardinalPosition == "south":
            self.south.newTransition(transition);
        else:
            self.west.newTransition(transition);
