
class direction:


    def __init__(self, direction):
        if direction.lower() == "east" or direction.lower() == "west" or direction.lower() == "north" or direction.lower() == "south":
            self.direction = direction;
            self.description = "";
            self.transition = None;
            self.items = [];
            self.events = [];
        else:
            raise Exception("Cardinal direction " + direction + " is not a valid direction.");


    def newTransition(self, transition):
        #print transition.name;
        self.transition = transition;
