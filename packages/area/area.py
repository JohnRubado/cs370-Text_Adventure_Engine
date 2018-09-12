from packages.item import item;
from enum import Enum;

class Area:

    
    transitions = None;
    items = [];

    def __init__(self,name):
        self.name = name;
        self.transitions = [None,None,None,None];

    def newItem(self, item):
        print "TBD";

    def newTransition(self, transition):
        cardinalPosition = transition.cardinalPosition;

        if cardinalPosition == "N":
            self.transitions[transition_position.NORTH.value] = transition;
        elif cardinalPosition == "E":
            self.transitions[transition_position.EAST.value] = transition;
        elif cardinalPosition == "S":
            self.transitions[transition_position.SOUTH.value] = transition;
        else:
            self.transitions[transition_position.NORTH.value] = transition;

        #print self.name + " " +self.transitions[0].name;




class transition_position(Enum):
    NORTH = 0;
    EAST = 1;
    SOUTH = 2
    WEST = 3;
