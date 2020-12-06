import math
import sys
import logging

from lib.helpers import read_file, list_from_newline_sep_string

# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)

def count_group(group):
    yes = {}
    for i, person in enumerate(group):
        for question in person:
            if question not in yes:
                yes[question] = None
    return (len(yes.keys()))


def count_all_yes_group(group):
    log.debug(group)
    yes = {}
    for i, person in enumerate(group):
        for question in person:
            if question not in yes:
                yes[question] = [i]
            else:
                yes[question].append(i)
    log.debug(yes)
    all_yes_count = 0
    for answers_to_single_q in yes.values():
        if len(answers_to_single_q) == len(group):
            all_yes_count += 1
    return all_yes_count


def test_yes_counter():
    sample_input="""abc

a
b
c

ab
ac

a
a
a
a

b"""

    expected_groups = 5
    expected_yes_counts = [3, 3, 3, 1, 1]
    groups = list_from_newline_sep_string(sample_input)
    if len(groups) != 5:
        log.error("xx - group calculation wrong")
        log.error("got: '{}' expected: '{}'".format(len(groups), expected_groups))
    for i, group in enumerate(groups):
        yes_count = count_group(group)
        if yes_count != expected_yes_counts[i]:
            log.error("xx - group{} count_wrong".format(i))
            log.error("got: '{}' expected: '{}'".format(yes_count, expected_yes_counts[i]))

def test_all_yes_counter():
    sample_input="""abc

a
b
c

ab
ac

a
a
a
a

b"""

    expected_groups = 5
    expected_yes_counts = [3, 0, 1, 1, 1]
    groups = list_from_newline_sep_string(sample_input)
    if len(groups) != 5:
        log.error("xx - group calculation wrong")
        log.error("got: '{}' expected: '{}'".format(len(groups), expected_groups))
    for i, group in enumerate(groups):
        yes_count = count_all_yes_group(group)
        if yes_count != expected_yes_counts[i]:
            log.error("xx - group {} count_wrong".format(i))
            log.error("got: '{}' expected: '{}'".format(yes_count, expected_yes_counts[i]))
            break

def part1():
    lines = read_file(split_lines=False)
    groups = list_from_newline_sep_string(lines)
    total = 0
    for group in groups:
        total += count_group(group)
    print(total)


def part2():
    lines = read_file(split_lines=False)
    groups = list_from_newline_sep_string(lines)
    total = 0
    for group in groups:
        total += count_all_yes_group(group)
    print(total)

def main():
    # test_yes_counter()
    part1()
    # test_all_yes_counter()
    part2()


if __name__ == "__main__":
    sys.exit(main())
