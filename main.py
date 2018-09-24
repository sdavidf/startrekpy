#Startrek.py
#A conversion of the old mainframe grid-based space game
#sdf, 2018

#imports as needed
from math import sqrt
from models import starship
import random
import map

#right now the map is a global, might change later
map = PlayField.initMap(8,8)

#let's make an example starship
enterprise = starship("enterprise", 100, 100, 100, 100, 3, 3)
klingon = starship("d'var", 100, 100, 100, 100, 6, 2)

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

def KlingonAI():
    """
    I don't know if you can call an RNG an AI, but we're going
    to start with this and see where we go...
    """
    move = random.randint(0,2)
    if move == 0:
        klingon.move(random.randint(1,8), random.randint(1,8))
    elif move == 1:
        klingon.phaser_attack(enterprise, random.randint(20, 50))
    elif move == 2:
        klingon.photon_attack(enterprise, random.randint(10, 50))
    else:
        print("")

def gameLoop():
    """
    INCOMPLETE: the main interactive loop
    """
    #TODO: Move prompt into own function
    drawDisplay()
    prompt = input("Enter your command, Captain. (MOVE, PHASERS or PHOTONS)")
    if prompt == "MOVE" or "move":
        inputX = input("Enter X coordinate 1-8: ")
        inputY = input("Enter Y coordinate 1-8: ")
        enterprise.move(int(inputX), int(inputY))
    elif prompt == "PHASERS" or "phasers":
        inputStrength = input("Enter strength of phaser attack 1-100: ")
        enterprise.phaser_attack(klingon, int(inputStrength))
    elif prompt == "PHOTONS" or "photons":
        inputStrength = input("Enter strength of photon attack 1-100: ")
        enterprise.photon_attack(klingon, int(inputStrength))
    else:
        print("Try again.")
        gameLoop()
    KlingonAI()
    gameLoop()

initMap(8,8)
gameLoop()
#testscript()
