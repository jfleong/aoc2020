from aoc.day_10.main import create_chain, count_all_arrangements, get_jolt_diffs
from aoc.day_10.main import count_all_arrangements_v2


def test_create_chain():
    sample_input="""16
10
15
5
1
11
7
19
6
12
4"""
    expected_output_joltage = 22
    resulting_chain = create_chain(sample_input.split("\n"))

def test_get_jolt_diffs():
    sample_input="""16
10
15
5
1
11
7
19
6
12
4"""
    expected_1jolt_diffs = 7
    expected_2jolt_diffs = 0
    expected_3jolt_diffs = 5
    chain = create_chain(sample_input.split("\n"))
    jolt_diffs = get_jolt_diffs(chain)

    assert jolt_diffs[1] == expected_1jolt_diffs
    assert jolt_diffs[2] == expected_2jolt_diffs
    assert jolt_diffs[3] == expected_3jolt_diffs

def test_find_total_arrangements():
    sample_input="""16
10
15
5
1
11
7
19
6
12
4"""
    expected_arrangements = 8

    chain = create_chain(sample_input.split("\n"))
    arrangements = count_all_arrangements(chain)
    assert arrangements == expected_arrangements

def test_find_total_optimized():
    # XXX TODO: fix this
    # XXX TODO: fix this
    # XXX TODO: fix this
    # XXX TODO: fix this
    # XXX TODO: fix this
    return
    sample_input="""16
10
15
5
1
11
7
19
6
12
4"""
    expected_arrangements = 8

    chain = create_chain(sample_input.split("\n"))
    arrangements = count_all_arrangements_v2(chain)
    assert arrangements == expected_arrangements

    longer_input="""28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
    expected_arrangements = 19208

    chain = create_chain(longer_input.split("\n"))
    arrangements = count_all_arrangements_v2(chain)
    assert arrangements == expected_arrangements


