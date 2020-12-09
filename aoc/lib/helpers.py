import requests

def read_file(path="input.txt", split_lines=True):
    with open(path) as f:
        if split_lines:
            return f.read().splitlines()
        else:
            return f.read()

def fetch_input(day, year=2020, to_file=False):
    resp = requests.get("https://adventofcode.com/{}/day/{}/input".format(year, day))
    if to_file:
        with open(to_file, "w") as f:
            f.write(resp.text)
    return resp.text

def list_from_newline_sep_string(newline_sep_string):
    """ returns list of lists
    """
    groups = []
    for group_items in newline_sep_string.split("\n\n"):
        groups.append(group_items.split("\n"))
    return groups

def find_summer(target, numbers):
    num_map = {}
    for number in numbers:
        number = int(number)
        difference = target - number
        if number in num_map:
            return number * num_map[number]
        num_map[difference] = number

    return -1
