from aoc.day_08.main import find_loop, fix_loop

sample_input="""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

def test_find_loop():
    expected_acc = 5
    pos, acc = find_loop(sample_input.split("\n"))
    assert acc == expected_acc

def test_nop_jmp_alter():
    expected_acc = 8
    pos, acc = fix_loop(sample_input.split("\n"))
    assert acc == expected_acc

