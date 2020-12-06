from aoc.lib.helpers import list_from_newline_sep_string

def test_list_from_newline_sep_string():
    sample_input="""abc

    a
    a
    a"""

    expected_len = 2
    new_list = list_from_newline_sep_string(sample_input)
    assert len(new_list) == 2
