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

def test_list_from_newline_sep_string():
    sample_input="""abc

    a
    a
    a"""

    expected_len = 2
    new_list = list_from_newline_sep_string(sample_input)
    if len(new_list) != 2:
        log.error("xxx - wrong amount of groups")
        log.error(new_list)

def main():
   test_list_from_newline_sep_string()

if __name__ == "__main__":
    main()
