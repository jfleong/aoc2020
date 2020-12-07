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

def find_possible_bags(start, graph):
    return -1
