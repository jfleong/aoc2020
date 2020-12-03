import logging
import sys

from lib.helpers import read_file

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)


def part_one(numbers):
    num_map = {}
    for number in numbers:
        number = int(number)
        difference = 2020 - number
        if number in num_map:
            log.info("{} + {}".format(number, num_map[number]))
            log.info(number * num_map[number])
            return number * num_map[number]
        num_map[difference] = number

    return -1


def part_two(numbers):
    for number_third in numbers:
        number_third = int(number_third)
        num_map = {}
        for number in numbers:
            number = int(number)
            difference = 2020 - number - number_third
            if number in num_map:
                log.info("{} + {} + {}".format(number_third, number, num_map[number]))
                log.info(number * num_map[number] * number_third)
                return
            num_map[difference] = number


def main():
    numbers = read_file("puzzle_inputs.txt")
    part_one(numbers)
    part_two(numbers)

if __name__ == "__main__":
    sys.exit(main())
