from aoc.day_12.main import compute_manhattan
from aoc.day_12.main import move_ship
from aoc.day_12.main import part2_move


def test_short_move():
    moves=["F10", "N3", "F7", "R90", "F11"]

    final_pos = move_ship(moves)
    expected_manhattan = 25
    assert compute_manhattan(final_pos) == expected_manhattan

def test_short_move_waypoint():
    moves=["F10", "N3", "F7", "R90", "F11"]

    final_pos = part2_move(moves)
    expected_manhattan = 286
    assert compute_manhattan(final_pos) == expected_manhattan
