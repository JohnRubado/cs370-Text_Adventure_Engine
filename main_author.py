from packages.adventure import *;


myWorld = world("A brand new world!")
myWorld.newArea("forest", "It is Woody around here");
myWorld.newArea("quarry", "A lot of rocks are here");
myWorld.newArea("trail", "OH F*** A GRIZZLY");

myWorld.newTransition("portal","forest", "quarry", "south", ["teleport"], True);
myWorld.newTransition("portal","quarry", "trail", "west", ["teleport"], True);
#myWorld.newTransition("Ladder", "trail","quarry","West", ["climb"], True);

myWorld.movePlayer("south");
myWorld.movePlayer("west");
myWorld.look();
