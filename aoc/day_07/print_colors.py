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


def part1():
    graph = create_graph(read_file(split_lines=False))
    colors = {}
    for key, values in graph.items():
        colors[key] = None
        for value in values:
            colors[value] = None
    adjectives = {}
    names = {}
    for color in colors.keys():
        adjective = color.split(" ")[0]
        adjectives[adjective] = None
        name = color.split(" ")[1]
        names[name] = None
    from pprint import pprint
    pprint(sorted(adjectives.keys()))
    pprint(sorted(names.keys()))

def main():
    part1()

if __name__ == "__main__":
    sys.exit(main())
