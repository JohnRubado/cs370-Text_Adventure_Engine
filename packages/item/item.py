from packages.action import action;

class item:

    possibleActions = [];

    def __init__(self, name):
        this.name = name;
        this.possibleActions = [];

    def addAction(self, action):
        this.possibleActions.append(action);
