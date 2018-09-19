#!/bin/env pyhton3
from packages.adventure import *

class parser:
    def __init__(self, world):
        self.world = world

    def start(self):
        print self.world.name;
        while(True):
            userInput = raw_input()
            print "";
            userInput = userInput.lower().split()
            moveKeywords = ["move","go"]
            lookKeywords = ["look", "show"]
            noiseWords = ["at", "am", "here", "there"]
            for word in noiseWords:
                if word in userInput:
                    userInput.remove(word)
            if userInput[0] in moveKeywords:
                argument = ' '.join(userInput[1:])
                self.world.movePlayer(argument)

            elif userInput[0] in lookKeywords:
                argument = ' '.join(userInput[1:])
                if argument is '':
                    self.world.look()
                else:
                    self.world.look(argument)
