import sys
import logging

from lib.helpers import read_file

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger(__name__)

def find_loop(input_lines):
    boot_code = input_lines
    acc = 0
    position_log = []
    start = 0
    i = 0
    while True:
        log.debug("entering while")
        for i in range(start, len(boot_code)):
            if i in position_log:
                return i, acc
            position_log.append(i)

            action = boot_code[i].split(" ")[0]
            number= int(boot_code[i].split(" ")[1])
            log.debug("acc: {}".format(acc))
            log.debug("i: {}".format(i))
            log.debug("-- action: {}".format(action))
            log.debug("-- number: {}".format(number))
            if action == "acc":
                acc += number
            elif action == "jmp":
                # f*ck it... this works
                if i == len(boot_code) - 1:
                    return i, acc
                start = i + number
                break
            elif action == "nop":
                pass
            else:
               log.error("invalid move {}".format(action))
            if i == len(boot_code) - 1:
                return i, acc


def fix_loop(input_lines):
    start = 0
    while True:
        for i in range(start, len(input_lines)):
            line = input_lines[i]
            action = line.split(" ")[0]
            number = line.split(" ")[1]
            if i == 0 and action == "nop":
                continue
            if action == "nop":
                new_action = "jmp"
            elif action == "jmp":
                new_action = "nop"
            else:
                continue

            log.debug("changing pos: {} from {} to {}".format(
                i,
                action,
                new_action))
            boot_code = input_lines[:]
            boot_code[i] = "{} {}".format(new_action, number)
            finish_pos, acc = find_loop(boot_code)
            if finish_pos == len(input_lines) - 1:
                return finish_pos, acc
    return 0, 1

def part1():
    i, acc = find_loop(read_file())
    print(acc)

def part2():
    i, acc = fix_loop(read_file())
    print(acc)
    pass

def main():
    # part1()
    part2()

if __name__ == "__main__":
    sys.exit(main())
