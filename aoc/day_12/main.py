import logging
import sys

from lib.helpers import read_file

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)

def compute_manhattan(position):
    return abs(position[0]) + abs(position[1])

def turn_ship(curr_facing, move):
    direction = move[0]
    amount = int(move[1:])
    if curr_facing == "N":
        if amount == 90:
            if direction == "L":
                return "W"
            else:
                return "E"
        if amount == 180:
            return "S"
        if amount == 270:
            if direction == "L":
                return "E"
            else:
                return "W"
    elif curr_facing == "E":
        if amount == 90:
            if direction == "L":
                return "N"
            else:
                return "S"
        if amount == 180:
            return "W"
        if amount == 270:
            if direction == "L":
                return "S"
            else:
                return "N"
    elif curr_facing == "S":
        if amount == 90:
            if direction == "L":
                return "E"
            else:
                return "W"
        if amount == 180:
            return "N"
        if amount == 270:
            if direction == "L":
                return "W"
            else:
                return "E"
    elif curr_facing == "W":
        if amount == 90:
            if direction == "L":
                return "S"
            else:
                return "N"
        if amount == 180:
            return "E"
        if amount == 270:
            if direction == "L":
                return "N"
            else:
                return "S"

def turn_waypoint(waypoint, move):
    direction = move[0]
    amount = int(move[1:])
    if amount == 90:
        if direction == "L":
            return [-1 * waypoint[1], waypoint[0]]
        else:
            return [waypoint[1], -1 * waypoint[0]]
    if amount == 180:
        return [-1 * waypoint[0], -1 * waypoint[1]]
    if amount == 270:
        if direction == "L":
            return [waypoint[1], -1 * waypoint[0]]
        else:
            return [-1 * waypoint[1], waypoint[0]]


def move_ship(moves):
    curr_facing = "E"
    curr_pos = [0, 0]
    for move in moves:
        action = move[0]
        if action in ("L", "R"):
            curr_facing = turn_ship(curr_facing, move)
        elif action == "N":
            curr_pos[1] = curr_pos[1] + int(move[1:])
        elif action == "S":
            curr_pos[1] = curr_pos[1] - int(move[1:])
        elif action == "E":
            curr_pos[0] = curr_pos[0] + int(move[1:])
        elif action == "W":
            curr_pos[0] = curr_pos[0] - int(move[1:])
        elif action == "F":
            if curr_facing == "N":
                curr_pos[1] = curr_pos[1] + int(move[1:])
            elif curr_facing == "S":
                curr_pos[1] = curr_pos[1] - int(move[1:])
            elif curr_facing == "E":
                curr_pos[0] = curr_pos[0] + int(move[1:])
            elif curr_facing == "W":
                curr_pos[0] = curr_pos[0] - int(move[1:])
    return curr_pos

def part2_move(moves):
    waypoint = [10,1]
    curr_pos = [0, 0]
    for move in moves:
        action = move[0]
        amount = int(move[1:])
        if action in ("L", "R"):
            waypoint = turn_waypoint(waypoint, move)
        elif action == "N":
            waypoint[1] = waypoint[1] + amount
        elif action == "S":
            waypoint[1] = waypoint[1] - amount
        elif action == "E":
            waypoint[0] = waypoint[0] + amount
        elif action == "W":
            waypoint[0] = waypoint[0] - amount
        elif action == "F":
            curr_pos[0] = curr_pos[0] + amount * waypoint[0]
            curr_pos[1] = curr_pos[1] + amount * waypoint[1]
    return curr_pos

def part1():
    final_pos = move_ship(read_file())
    print(compute_manhattan(final_pos))

def part2():
    final_pos = part2_move(read_file())
    print(compute_manhattan(final_pos))

def main():
    part1()
    part2()

if __name__ == "__main__":
    sys.exit(main())
