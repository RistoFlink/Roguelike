import numpy as np #type: ignore
from tcod.console import Console

import tile_types

class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")

        self.visible = np.full((width, height), fill_value=False, order="F") #tiles the player can currently see
        self.explored = np.full((width, height), fill_value=False, order="F") #tiles the player has seen before

    def in_bounds(self, x: int, y: int) -> bool:
        #return true if x and y are not outside the bounds of the map
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        #renders the map
        #if tile is in "visible" array -> draw it with "light"
        #if it isn't but has been explored -> "dark"
        #otherwise draw it with "SHROUD"
        console.tiles_rgb[0:self.width, 0:self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=tile_types.SHROUD
        )