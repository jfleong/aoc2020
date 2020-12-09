from aoc.day_09.main import  find_consecutive_sum, find_first_invalid

sample_input="""35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

def test_find_first_invalid():
    preamble = 5
    expected_incorrect = 127
    first_invalid = find_first_invalid(sample_input.split("\n"), preamble)
    assert first_invalid == expected_incorrect

def test_cons_sum():
    preamble = 5
    expected_incorrect = 127
    expected_sum = 62
    first_invalid = find_consecutive_sum(sample_input.split("\n"), expected_incorrect)
    assert first_invalid == expected_sum

