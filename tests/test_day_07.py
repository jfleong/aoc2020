from aoc.day_07.main import create_graph, find_possible_bags
from aoc.lib.helpers import list_from_newline_sep_string


def test_create_graph():
    sample_rules="""light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
    expected_output = {
        "light red": ["bright white", "muted yellow", "muted yellow"],
        "dark orange": ["bright white", "bright white", "bright white", "muted yellow", "muted yellow", "muted yellow", "muted yellow"],
        "bright white": ["shiny gold"],
        "muted yellow": ["shiny gold", "shiny gold", "faded blue", "faded blue", "faded blue", "faded blue", "faded blue", "faded blue", "faded blue", "faded blue", "faded blue"],
        "shiny gold": ["dark olive", "vibrant plum", "vibrant plum"],
        "dark olive": ["faded blue", "faded blue", "faded blue", "dotted black", "dotted black", "dotted black", "dotted black"],
        "vibrant plum": ["faded blue", "faded blue", "faded blue", "faded blue", "faded blue", "dotted black", "dotted black", "dotted black", "dotted black", "dotted black", "dotted black"],
        "faded blue": [],
        "dotted black": []
    }
    graph = create_graph(sample_rules)
    assert graph == expected_output

def test_find_possible_bags():
    sample_rules="""light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
    sample_input = "1 shiny golden bag"
    graph = create_graph(sample_rules)
    assert find_possible_bags(sample_input, graph) == 4
