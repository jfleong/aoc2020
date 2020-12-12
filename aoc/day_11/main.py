import logging
import sys

from lib.helpers import read_file

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)

def create_seat_map(input_lines):
    seat_map = []
    for row in input_lines:
        seat_map.append([char for char in row])
    return seat_map

def get_map_string(seat_map):
    retval = ""
    for row in seat_map:
        retval += "".join(row)
        retval += "\n"
    return retval.strip()

def count_occupied(seat_map):
    occupied = 0
    for row in seat_map:
        for col in row:
            if col == "#":
                occupied += 1
    return occupied

def count_occupied_visible(seat_map, row_pos, col_pos):
    max_row = len(seat_map) - 1
    max_col = len(seat_map[0]) - 1
    # count adjacent occupied
    occupied_visible = 0
    visible_paths=dict(
        n=(row_pos - 1, col_pos),
        ne=(row_pos -1, col_pos + 1),
        e=(row_pos, col_pos + 1),
        se=(row_pos + 1, col_pos + 1),
        s=(row_pos + 1, col_pos),
        sw=(row_pos + 1, col_pos - 1),
        w=(row_pos, col_pos - 1),
        nw=(row_pos - 1, col_pos - 1),
    )
    for direction, points in visible_paths.items():
        row = points[0]
        col = points[1]
        if row < 0 or row > max_row:
            continue
        if col < 0 or col > max_col:
            continue
        looking_at = seat_map[row][col]
        if looking_at == "#":
            occupied_visible += 1
            continue
        elif looking_at == "L":
            continue

        if direction == "n":
            row -= 1
            while row >= 0:
                looking_at = seat_map[row][col]
                if looking_at == "#":
                    occupied_visible += 1
                    break
                elif looking_at == "L":
                    break
                row -= 1
        elif direction == "ne":
            row -= 1
            col += 1
            while row >= 0 and col <= max_col:
                looking_at = seat_map[row][col]
                if looking_at == "#":
                    occupied_visible += 1
                    break
                elif looking_at == "L":
                    break
                row -= 1
                col += 1
        elif direction == "e":
            col += 1
            while col <= max_col:
                looking_at = seat_map[row][col]
                if looking_at == "#":
                    occupied_visible += 1
                    break
                elif looking_at == "L":
                    break
                col += 1
        elif direction == "se":
            row += 1
            col += 1
            while row <= max_row and col <= max_col:
                looking_at = seat_map[row][col]
                if looking_at == "#":
                    occupied_visible += 1
                    break
                elif looking_at == "L":
                    break
                row += 1
                col += 1
        elif direction == "s":
            row += 1
            while row <= max_row:
                looking_at = seat_map[row][col]
                if looking_at == "#":
                    occupied_visible += 1
                    break
                elif looking_at == "L":
                    break
                row += 1
        elif direction == "sw":
            row += 1
            col -= 1
            while row <= max_row and col >= 0:
                looking_at = seat_map[row][col]
                if looking_at == "#":
                    occupied_visible += 1
                    break
                elif looking_at == "L":
                    break
                row += 1
                col -= 1
        elif direction == "w":
            col -= 1
            while col >= 0:
                looking_at = seat_map[row][col]
                if looking_at == "#":
                    occupied_visible += 1
                    break
                elif looking_at == "L":
                    break
                col -= 1
        elif direction == "nw":
            row -= 1
            col -= 1
            while row >= 0 and col >= 0:
                looking_at = seat_map[row][col]
                if looking_at == "#":
                    occupied_visible += 1
                    break
                elif looking_at == "L":
                    break
                row -= 1
                col -= 1
    return occupied_visible

def get_seat_change(seat_map, row_pos, col_pos, visibility=False):
    # Return Floor
    current_seat = seat_map[row_pos][col_pos]
    if current_seat == ".":
        return current_seat

    occupied = 0
    # count adjacent occupied
    if not visibility:
        occ_threshold = 4
        for row in range(row_pos-1, row_pos + 2):
            if row < 0 or row > len(seat_map) - 1:
                continue
            for col in range(col_pos -  1, col_pos + 2):
                if col < 0 or col > len(seat_map[row]) - 1:
                    continue
                if row == row_pos and col == col_pos:
                    continue
                if seat_map[row][col] == "#":
                    occupied += 1
    else:  # part 2
        occ_threshold = 5
        occupied = count_occupied_visible(seat_map, row_pos, col_pos)

    # Do the maths
    if current_seat == "L":
        if not occupied:
            return "#"
    if current_seat == "#":
        if occupied >= occ_threshold:
            return "L"

    # nothing meets the change requirements
    return current_seat


def apply_round(seat_map, visibility=False):
    new_map = []
    for i in range(len(seat_map)):
        new_row = []
        for j in range(len(seat_map[i])):
            new_row.append(get_seat_change(seat_map, i, j, visibility))
        new_map.append(new_row)
    return new_map

def apply_all_rounds(seat_map, visibility=False):
    new_map = None
    maps_differ = True
    while maps_differ:
        # first round we can skip this
        new_seat_map = apply_round(seat_map, visibility)
        if new_seat_map == seat_map:
            break
        seat_map = new_seat_map
    return new_seat_map

def part1():
    seat_map = create_seat_map(read_file())
    end_map = apply_all_rounds(seat_map)
    print(count_occupied(end_map))

def part2():
    seat_map = create_seat_map(read_file())
    end_map = apply_all_rounds(seat_map, visibility=True)
    print(count_occupied(end_map))
    pass

def main():
    part1()
    part2()

if __name__ == "__main__":
    sys.exit(main())
