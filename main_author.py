from packages.adventure import *;


myWorld = world("A brand new world!")
myWorld.newArea("forest");
myWorld.newArea("quarry");
myWorld.newArea("trail");

myWorld.newTransition("portal","forest", "quarry", "North", ["teleport"], True);
myWorld.newTransition("Ladder", "trail","quarry","West", ["climb"], True);
myWorld.printWorld();
