import math
import sys
import logging

from lib.helpers import read_file

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger(__name__)


class BoardingPass(object):
    def __init__(self, boarding_pass_string):
        # 128 rows
        self.row_string = boarding_pass_string[:7]
        # 8 columns
        self.column_string = boarding_pass_string[-3:]
        self.row = self.compute_row()
        self.column = self.compute_column()
        self.seat_id = self.row * 8 + self.column

    def compute_row(self):
        return search(self.row_string, 0, 127)

    def compute_column(self):
        return search(self.column_string, 0, 7)


def search(bp_string, minimum, maximum):
    pop = bp_string[0]
    left = False
    if pop in ["F", "L"]:
        left = True
    if len(bp_string) == 1:
        return minimum if left else maximum
    if left:
        middle = minimum + (maximum - minimum) / 2
        return search(bp_string[1:], minimum, middle)
    else:
        middle = minimum + (maximum - minimum) / 2 + 1 # this'll just work
        return search(bp_string[1:], middle, maximum)

def test_bp_init():
    test_data = dict(
        BFFFBBFRRR=dict(row=70,column=7,ID=567),
        FFFBBBFRRR=dict(row=14,column=7,ID=119),
        BBFFBBFRLL=dict(row=102,column=4,ID=820),
    )
    for key, evs in test_data.items():
        bp = BoardingPass(key)
        if bp.row != evs["row"]:
            log.error("WRONG ROW: {}, expected: {}".format(bp.row, evs["row"]))
        if bp.column != evs["column"]:
            log.error("WRONG column: {}, expected: {}".format(bp.column, evs["column"]))
        if bp.seat_id != evs["ID"]:
            log.error("WRONG seat_id: {}, expected: {}".format(bp.seat_id, evs["ID"]))


def part_one():
    log.info("--part one--")
    bp_string_list = read_file()
    highest_id = -1
    for bp_string in bp_string_list:
        bp = BoardingPass(bp_string.strip())
        if bp.seat_id > highest_id:
            highest_id = bp.seat_id

    log.info("highest_id: '{}'".format(highest_id))

def part_two():
    log.info("--part two--")
    bp_string_list = read_file()
    seat_map = [[column for column in range(8)] for row in range(128)]
    for bp_string in bp_string_list:
        bp = BoardingPass(bp_string.strip())
        seat_map[bp.row][bp.column] = "x"
    for row in range(128):
        for column in range(8):
            if seat_map[row][column] != "x":
                if column == 7:
                    if seat_map[row][column-1] == "x":
                        print("my_seat_id: {}".format(row * 8 + column))
                elif column == 0:
                    if seat_map[row][column+1] == "x":
                        print("my_seat_id: {}".format(row * 8 + column))
                else:
                    if seat_map[row][column+1] == "x" and \
                        seat_map[row][column-1] == "x":
                        print("my_seat_id: {}".format(row * 8 + column))



def main():
    test_bp_init()
    part_one()
    part_two()



if __name__ == "__main__":
    sys.exit(main())
