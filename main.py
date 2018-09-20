#Startrek.py
#A conversion of the old mainframe grid-based space game
#sdf, (c) 2018

#imports as needed
from math import sqrt
from models import starship
import random

#right now the map is a global, might change later
map = []



#let's make an example starship
enterprise = starship("enterprise", 100, 100, 100, 100, 3, 3)
klingon = starship("d'var", 100, 100, 100, 100, 6, 2)


def initMap(xsize, ysize):
    """
    This creates an 8x8 single grid map, the acual game uses an 8x8 array of 8x8 local maps
    """
    for i in range(xsize):
        map.append([])
        for j in range(ysize):
            map[i].append(".")

def printHUD():
    """
    This displays the HUD at the start of each return
    """
    HUDDisplay = f"USS {enterprise.name} - SHIELDS {enterprise.shields} -" \
                 f"HULL {enterprise.hull} - PHASER ENERGY {enterprise.phaser} -"\
                 f"TORPEDOS {enterprise.photons} - LOCATION {enterprise.location}"
    print(HUDDisplay)

def printMap():
    """
    This puts our local map on the screen and plots the location of the ships
    """
    map[enterprise.coordX-1][enterprise.coordY-1] = "E"
    map[klingon.coordX-1][klingon.coordY-1] = "K"
    print("The enterprise is at: " + str(enterprise.location))
    for i in range(len(map)):
        print(map[i])

def drawDisplay():
    """
    On each turn, draws the HUD and the Map on the terminal. May also become
    home to ship-redraw code from the move method once system is interactive.
    """
    printHUD()
    printMap()

def testscript():
    """
    A chunk of prescripted sequences used for testing new methods
    """
    initMap(8,8)
    drawDisplay()
    enterprise.move(5, 4)
    klingon.move(5, 3)
    klingon.phaser_attack(enterprise, 20)
    print(enterprise.shields)

def gameLoop():
    """
    INCOMPLETE: the main interactive loop
    """
    #TODO: Move prompt into own function
    #TODO: Write code to control Klingon behavior
    drawDisplay()
    prompt = input("Enter your command, Captain. (MOVE or ATTACK)")
    if prompt == "MOVE":
        inputX = input("Enter X coordinate 1-8")
        inputY = input("Enter Y coordinate 1-8")
        enterprise.move(int(inputX), int(inputY))
    elif prompt == "ATTACK":
        inputStrength = input("Enter strength of phaster attack 1-100")
        enterprise.phaser_attack(klingon, int(inputStrength))
    else:
        print("Try again.")
        gameLoop()
    gameLoop()

initMap(8,8)
gameLoop()
#testscript()
