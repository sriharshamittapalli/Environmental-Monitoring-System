# Implemented all important functions in commonutils.
from commonutils import *

def tile_component(tiles_list):
    if tiles_list:
        if tiles_list[0]:
            if tiles_list[1]:
                if tiles_list[2]:
                    if tiles_list[3]:
                        tiles_list[0],tiles_list[1],tiles_list[2],tiles_list[3] = columns(len(tiles_list))
                        tiles_list[0] = empty(tiles_list[0])
                        tiles_list[1] = empty(tiles_list[1])
                        tiles_list[2] = empty(tiles_list[2])
                        tiles_list[3] = empty(tiles_list[3])
    return tiles_list[0], tiles_list[1], tiles_list[2], tiles_list[3]
