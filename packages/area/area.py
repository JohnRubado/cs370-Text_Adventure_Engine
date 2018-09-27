from packages.item import item;
from packages.direction.direction import direction;


class Area:

    transitions = None;

    directions = None;
    north = None;
    east = None;
    south = None;
    west = None;

    def __init__(self,name, description = "A vast land of wonders, maybe I should take a look around?"):
        self.name = name;
        self.items = [];
        self.north = direction("north");
        self.east = direction("east");
        self.south = direction("south");
        self.west = direction("west");
        self.description = description;
        self.directions = [None,None,None,None];
        self.directions[0] = self.north;
        self.directions[1] = self.east;
        self.directions[2] = self.south;
        self.directions[3] = self.west;

    def newItem(self, item):
        self.items.append(item)


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
