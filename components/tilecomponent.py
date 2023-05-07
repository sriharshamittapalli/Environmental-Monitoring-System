from commonutils import *

def tile_component(tiles_list):
    tiles_list[0],tiles_list[1],tiles_list[2],tiles_list[3] = columns(len(tiles_list))
    tiles_list[0] = empty(tiles_list[0])
    tiles_list[1] = empty(tiles_list[1])
    tiles_list[2] = empty(tiles_list[2])
    tiles_list[3] = empty(tiles_list[3])
    return tiles_list[0], tiles_list[1], tiles_list[2], tiles_list[3]