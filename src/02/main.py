import logging
import sys
import time

from lib.helpers import read_file

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger(__name__)

class PasswordLine(object):
    def __init__(self, policy_pass_string):
        self.policy = policy_pass_string.split(":")[0]
        self.password = policy_pass_string.split(":")[1].strip()

    def debug(self):
        log.info("policy: '{}'".format(self.policy))
        log.info("password: '{}'".format(self.password))

    def is_valid(self):
        occurance_min = int(self.policy.split(" ")[0].split("-")[0])
        occurance_max = int(self.policy.split(" ")[0].split("-")[1])
        occurance_count = self.password.count(self.policy.split(" ")[1])
        if occurance_count >= occurance_min and occurance_count <= occurance_max:
            return True
        return False

    def part2_is_valid(self):
        pos1 = int(self.policy.split(" ")[0].split("-")[0]) - 1
        pos2 = int(self.policy.split(" ")[0].split("-")[1]) - 1
        target = self.policy.split(" ")[1]
        found = False
        if pos1 <= len(self.password) and self.password[pos1] == target:
            found = True
        if pos2 <= len(self.password) and self.password[pos2] == target:
            if found:
                return False
            return True
        return found


def part_one(password_entries):
    valid_entries = 0
    for entry in password_entries:
        if PasswordLine(entry).is_valid():
            valid_entries += 1
    log.info("---valid_entries:")
    log.info(valid_entries)


def part_two(password_entries):
    valid_entries = 0
    for entry in password_entries:
        if PasswordLine(entry).part2_is_valid():
            valid_entries += 1
    log.info("---valid_entries:")
    log.info(valid_entries)

def main():
    password_entries = read_file()
    # part_one(password_entries)
    part_two(password_entries)

if __name__ == "__main__":
    sys.exit(main())
