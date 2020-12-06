from aoc.day_06.main import count_group, count_all_yes_group
from aoc.lib.helpers import list_from_newline_sep_string

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
    assert len(groups) == 5
    for i, group in enumerate(groups):
        yes_count = count_group(group)
        assert yes_count == expected_yes_counts[i]

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
