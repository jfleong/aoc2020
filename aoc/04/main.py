import sys
import logging

from lib.helpers import read_file

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger(__name__)

def make_passports(lines):
    passports = []
    passport = ""
    for line in lines:
        if len(line.strip()) == 0:
            pp_dict = {}
            for kv in passport.strip().split(" "):
                pp_dict[kv.split(":")[0]] = kv.split(":")[1]
            passports.append(pp_dict)

            passport = ""
            continue
        passport += " " + line
    # hey let's just add the last one
    pp_dict = {}
    for kv in passport.strip().split(" "):
        pp_dict[kv.split(":")[0]] = kv.split(":")[1]
    passports.append(pp_dict)
    return passports

def is_fake_valid(passport, super_valid=False):
    valid = True
    required_fields = (
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        # "cid",
    )
    for field in required_fields:
        if field not in passport.keys():
            return False

    if super_valid:
        for k, v in passport.items():
            valid = valid and field_valid(k, v)

    return valid

def year_validator(value, value_min, value_max):
    if len(value) != 4:
        return False
    value = int(value)
    if value >= value_min and value <= value_max:
        return True

def height_validator(value):
    units = value[-2:]
    amount = int(value[:-2])
    if units == "in":
        if amount >= 59 and amount <= 76:
            return True
    elif units == "cm":
        if amount >= 150 and amount <= 193:
            return True
    return False

def hex_validator(value):
    if not value.startswith("#"):
        return False
    if len(value) != 7:
        return False
    valid_values = [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
        "a", "b", "c", "d", "e", "f",
    ]
    for char in value.strip("#"):
        if char not in valid_values:
            return False
    return True

def field_valid(field, value):
    if field == "byr":
        return year_validator(value, 1920, 2002)
    elif field == "iyr":
        return year_validator(value, 2010, 2020)
    elif field == "eyr":
        return year_validator(value, 2020, 2030)
    elif field == "hgt":
        return height_validator(value)
    elif field == "hcl":
        return hex_validator(value)
    elif field == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif field == "pid":
        return len(value) == 9 and value.isdigit()
    elif field == "cid":
        return True
    else:
        log.error("invalid field: {}".format(field))



def test_is_fake_valid():
    test_input="""ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

    passport = ""
    valids = 0
    total = 0
    for passport in make_passports(test_input.split("\n")):
        if is_fake_valid(passport):
            valids += 1
    log.info(valids == 2)


def test_make_passports():
    test_input="""ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

    passport = ""
    valids = 0
    total = 0
    passports = make_passports(test_input.split("\n"))
    log.info(len(passports) == 4)

def part_one():
    valids = 0
    total = 0
    for passport in make_passports(read_file()):
        if is_fake_valid(passport):
            valids += 1
    log.info("VALIDS:")
    log.info(valids)

def part_two():
    valids = 0
    total = 0
    for passport in make_passports(read_file()):
        if is_fake_valid(passport, super_valid=True):
            valids += 1
    log.info("VALIDS:")
    log.info(valids)

def main():
    # test_is_fake_valid()
    # test_make_passports()
    part_one()
    part_two()

if __name__ == "__main__":
    sys.exit(main())
