import sys
import logging

from lib.helpers import read_file, list_from_newline_sep_string

# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)

def create_graph(input_text):
    # dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    graph = {}
    for line in input_text.split("\n"):
        if "contain" not in line:
            # my editor adds a newline eof
            continue
        node, leaves = line.split("contain")
        node_color = node[:-6]
        # Assuming that there can't be multiple rules for the same color
        graph[node_color] = []
        for leaf in leaves.split(","):
            parts = leaf.strip().split(" ")
            qty = parts[0]
            if qty == "no":
                break
            leaf_color = "{} {}".format(parts[1], parts[2])
            graph[node_color].extend([leaf_color for i in range(int(qty))])
    return graph


def can_hold(targets, graph, already_seen=[], total=0):
    color_can_hold_target = []
    for node, contents in graph.items():
        for color in targets:
            if color in contents and node not in already_seen:
                color_can_hold_target.append(node)
    if color_can_hold_target:
        uniques = list(set(color_can_hold_target))
        already_seen.extend(uniques)
        total += len(uniques)
        return can_hold(uniques, graph, already_seen, total)
    else:
        return total

def count_bags(targets, graph, total=0):
    bags_in_my_target = []
    for target in targets:
        if graph[target]:
            bags_in_my_target = graph[target]
            total += len(bags_in_my_target)
            for color in bags_in_my_target:
                total += count_bags([color], graph)
    return total

def part1():
    graph = create_graph(read_file(split_lines=False))
    target = "shiny gold"
    total = can_hold([target], graph)
    log.info(total)

def part2():
    graph = create_graph(read_file(split_lines=False))
    target = "shiny gold"
    total = count_bags([target], graph)
    log.info(total)

def main():
    part1()
    part2()

if __name__ == "__main__":
    sys.exit(main())
