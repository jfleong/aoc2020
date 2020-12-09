import sys
import logging

from lib.helpers import find_summer, read_file

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger(__name__)

def find_first_invalid(input_lines, preamble=25):
    preamble_list = input_lines[:preamble]
    for line in input_lines[preamble:]:
        found = find_summer(int(line), preamble_list)
        if found == -1:
            return int(line)
        preamble_list.pop(0)
        preamble_list.append(line)
    print("ran through")

def find_consecutive_sum(input_lines, target=1212510616):
    """
    XXX TODO: don't ever do this brute force shenanigans
    """
    start = 0
    while True:
        print("start = {}".format(start))
        if start >= len(input_lines) - 1:
            log.error("WE BROKE IT")
            return -1
        cons_lines = []
        for i in range (start, len(input_lines)):
            line = input_lines[i]
            cons_lines.append(int(line))
            cons_sum =  sum(cons_lines)
            if cons_sum == target:
                return int(sorted(cons_lines)[0]) + int(sorted(cons_lines)[-1])
            elif cons_sum > target:
                start = start + 1
                cons_lines.pop(0)
                break
                log.error("we went too far")
    return -1

def part1():
    print(find_first_invalid(read_file()))
def part2():
    print(find_consecutive_sum(read_file()))


def main():
    part1()
    part2()

if __name__ == "__main__":
    sys.exit(main())
