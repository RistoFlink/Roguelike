from typing import Tuple

import numpy as np # type: ignore'

#tile graphics structued type compatible with Console.titles_rgb
graphic_dt = np.dtype(
    [
        ("ch", np.int32), #Unicode sidepoint
        ("fg", "3B"), #3 unsigned bytes for RGB colours
        ("bg", "3B")
    ]
)

#tile struct used for statically defined tile data
tile_dt = np.dtype(
    [
        ("walkable", np.bool), #true if this tile can be walked over
        ("transparent", np.bool), #true if this tile doesn't block FOV
        ("dark", graphic_dt), #graphics for when this tile not in FOV
        ("light", graphic_dt), #graphics for when the tile is in FOV
    ]
)

def new_tile(
    *, #enforce the use of keywords so that parameter order doesn't matter
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    #helper function for defining individul tiles types
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)

#shroud represents unexplored and unseen tiles
SHROUD = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

floor = new_tile(
    walkable=True,
    transparent=True, 
    dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
    light=(ord(" "), (255, 255, 255), (200, 180, 50)),
)

wall = new_tile(
    walkable=False,
    transparent=False, 
    dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
    light=(ord(" "), (255, 255, 255), (130, 110, 50))
)