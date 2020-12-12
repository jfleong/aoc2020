from aoc.day_11.main import apply_all_rounds
from aoc.day_11.main import apply_round
from aoc.day_11.main import count_occupied
from aoc.day_11.main import count_occupied_visible
from aoc.day_11.main import create_seat_map
from aoc.day_11.main import get_map_string

def test_apply_all_round():
    """
    Wrote this after to make the tests match more the actual run
    """
    test_layout="""L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
    expected_end = """#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##"""
    seat_map = create_seat_map(test_layout.split("\n"))
    end_map = apply_all_rounds(seat_map)

    assert get_map_string(end_map) == expected_end

def test_count_occupied():
    input_map="""#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##"""

    expected_occupied = 37

    seat_map = create_seat_map(input_map.split("\n"))
    assert count_occupied(seat_map) == expected_occupied

def test_part_2_visibility():

    all_occupied = """.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#....."""
    row = 4
    col = 3
    expected_occupied = 8

    seat_map = create_seat_map(all_occupied.split("\n"))
    occupied_seats = count_occupied_visible(seat_map, row, col)
    assert occupied_seats == expected_occupied

    one_empty_seat = """.............
.L.L.#.#.#.#.
............."""
    row = 1
    col = 1
    expected_occupied = 0

    seat_map = create_seat_map(one_empty_seat.split("\n"))
    occupied_seats = count_occupied_visible(seat_map, row, col)
    assert occupied_seats == expected_occupied

    no_occupied_seats = """.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##."""
    row = 3
    col = 3

    expected_occupied = 0

    seat_map = create_seat_map(no_occupied_seats.split("\n"))
    occupied_seats = count_occupied_visible(seat_map, row, col)
    assert occupied_seats == expected_occupied

def test_part2_apply():
    test_layout="""L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
    expected_end = """#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#"""
    seat_map = create_seat_map(test_layout.split("\n"))
    end_map = apply_all_rounds(seat_map, visibility=True)

    assert get_map_string(end_map) == expected_end
    expected_count = 26
    assert count_occupied(end_map) == expected_count

