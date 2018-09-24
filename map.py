#map.py
#Separating out display and map generation into one fileself.
#sdf, 2018

class PlayField():
    """
    Methods and structures for the playfield and HUD.
    """
    def __init__(self, map):
        self.map = map


    def initMap(xsize, ysize):
        """
        This creates an 8x8 single grid map, the acual game uses an 8x8 array of 8x8 local maps
        """
        map = []
        for i in range(xsize):
            map.append([])
            for j in range(ysize):
                map[i].append(".")

    def drawDisplay():
        """
        On each turn, draws the HUD and the Map on the terminal. May also become
        home to ship-redraw code from the move method once system is interactive.
        """
        printHUD()
        printMap()
