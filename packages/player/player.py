
class player:

    name = "";

    def __init__(self, name="Player", description="",inventory=[]):
        self.description = description
        self.currentArea = None;
        self.name = name
        self.inventory = inventory
        self.isAlive = True

    def getCurrentRoom(self):
        return self.currentRoom

    def movePlayer(self):
        (canPass, message, room) = door.canPass(self)
        if canPass:
            self.currentRoom = room
        return (canPass, message)

    def getInventory(self):
        return self.inventory

    def getDescription(self, player):
        return "Your name is " + self.name + ". " + self.description
