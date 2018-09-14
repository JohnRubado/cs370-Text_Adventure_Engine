

class transition:

    def __init__(self,name,area,destination,cardinalPosition,possibleActions):
        self.name = name;
        self.message ="";
        self.area = area;
        self.destination = destination;
        self.cardinalPosition = cardinalPosition;
        if len(possibleActions) >= 1:
            self.possibleActions = possibleActions;
        else:
            self.possibleActions = ["use"];
