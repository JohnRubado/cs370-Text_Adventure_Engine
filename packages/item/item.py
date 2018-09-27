from packages.action import action;

class item:

    possibleActions = [];

    def __init__(self, name, description):
        self.name = name;
        self.description = description
        self.possibleActions = [];

    def addAction(self, action):
        self.possibleActions.append(action);
