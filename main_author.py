from packages.parser.parser import *;

myWorld = world("A beautiful world, maybe I should look around?","Johnny")
myWorld.newArea("forest", "It is Woody around here");
myWorld.newArea("quarry", "A lot of rocks are here");
myWorld.newArea("trail", "AHHH A GRIZZLY!!");
myWorld.newArea("river", "I can barely touch!");
myWorld.setStart("quarry");

myWorld.newTransition("portal","forest", "quarry", "south", ["teleport"], True);
myWorld.newTransition("portal","quarry", "trail", "west", ["teleport"], True);
myWorld.newTransition("ladder","trail", "river", "west", ["climb"], False);

myWorld.newItem(" A Key"," Its a fucking key","river");

parser = parser(myWorld);
parser.start();
