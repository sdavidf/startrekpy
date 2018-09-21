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
