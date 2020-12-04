import sys
import logging

from lib.helpers import read_file

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger(__name__)

def traverse(x, y):
    log.info("slope: {}/{}".format(y,x))
    rows = read_file()
    curpos = 0
    trees = 0
    for i in range(y, len(rows), y):
        row = rows[i]
        curpos = (curpos + x)
        if curpos > 30:
            curpos = curpos % 31
        if row[curpos] == "#":
            trees += 1
    log.info("-- trees --")
    log.info(trees)
    return trees

def part1():
    total = traverse(3, 1)
    log.info("TOTAL:")
    log.info(total)

def part2():
    total = traverse(1, 1)*traverse(3, 1)*traverse(5, 1)*traverse(7, 1)*traverse(1, 2)
    log.info("TOTAL:")
    log.info(total)

def main():
    # 323 total rows
    # 30 row length
    # assume all rows are the same length
    part1()
    part2()

if __name__ == "__main__":
    sys.exit(main())


if __name__ == "__main__":
    sys.exit(main())

