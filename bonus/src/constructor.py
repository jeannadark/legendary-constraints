import numpy as np


def construct_landscape(data: str, start_string: str = 'Landscape\n', end_string: str = '\n# Tiles') -> np.array:

    # count number of columns for matrix
    data = data.split(start_string)[-1].split(end_string)[0]
    first_row = data.split(" \n")[0].split("  ")
    cnt = 0
    for ele in first_row:
        splitted_str = ele.split(" ")
        for i in splitted_str:
            cnt += 1

    # construct a cnt x cnt matrix
    mat = np.empty([cnt, cnt], dtype=object)
    for i in range(0, cnt):
        row = data.split(" \n")[i].split("  ")
        j = 0
        for ele in row:
            splitted_str = ele.split(" ")
            for string in splitted_str:
                mat[i][j] = string
                j += 1
    return mat


def parse_number_of_tiles(data: str, start_string: str = '\n# Tiles: \n', end_string = '\n') -> dict:

    data = data.split(start_string)[-1].split(end_string)[0]
    outer_boundary = int(data.split('OUTER_BOUNDARY')[-1].split(',')[0].replace('=', ''))
    el_shape = int(data.split('EL_SHAPE')[-1].split(',')[0].replace('=', ''))
    full_block = int(data.split('FULL_BLOCK')[-1].split('}')[0].replace('=', ''))
    tiles = dict()
    tiles['outer_boundary'] = outer_boundary
    tiles['el_shape'] = el_shape
    tiles['full_block'] = full_block

    return tiles


def parse_targets(data: str, start_string: str = '\n# Targets: \n', end_string: str = '\n') -> dict:

    data = data.split(start_string)[-1].split(end_string)
    targets = dict()
    for i in range(0, 4):
        trg = data[i].split(':')
        targets[trg[0]] = int(trg[1])

    return targets
