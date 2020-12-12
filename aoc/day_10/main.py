import logging
import sys

from lib.helpers import read_file

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)

def create_chain(input_lines):
    sorted_chain = sorted([ int(line) for line in input_lines])
    sorted_chain.insert(0, 0)
    sorted_chain.append(sorted_chain[-1] + 3)
    return sorted_chain

def get_jolt_diffs(adapter_chain):
    jolt_diffs = {
        1: 0,
        2: 0,
        3: 0,
    }
    for i in range(len(adapter_chain) - 2):
        adapter = adapter_chain[i]
        next_adapter = adapter_chain[i+1]
        jolt_diffs[next_adapter - adapter] += 1
    jolt_diffs[3] += 1
    return jolt_diffs

def count_all_arrangements(chain, arrangements={}):
    if not arrangements:
        chain.insert(0, 0)
        chain.append(chain[-1] + 3)
        arrangements[" ".join([str(adapter) for adapter in chain])] = 1
    for i in range(len(chain) - 3):
        item = chain[i]
        diff = chain[i+2] - item
        if diff > 1 and diff <= 3:
            new_chain = chain[:]
            del new_chain[i+1]
            if " ".join([str(adapter) for adapter in new_chain]) in arrangements:
                continue
            arrangements[" ".join([str(adapter) for adapter in new_chain])] = 1
            count_all_arrangements(new_chain, arrangements)

    return len(arrangements)

def count_all_arrangements_v2(chain, start=0):
    # count this chain
    arrangements = 1
    # for i, item in enumerate(chain):
    for i in range(start, len(chain) - 2):
        item = chain[i]
        skip = chain[i+2] - item
        skip2 = -1
        new_chain = chain[:]
        if i + 3 < len(chain) -1:
            skip2 = chain[i+3] - item
        if skip <= 3:
            del new_chain[i+1]
            arrangements += 1
            if skip2 == 3:
                del new_chain[i+1]
            arrangements += count_all_arrangements_v2(new_chain, start=i)
    return arrangements


def part1():
    chain = create_chain(read_file())
    jolt_diffs = get_jolt_diffs(chain)
    print(jolt_diffs[1] * jolt_diffs[3])
    pass

def part2():
    chain = create_chain(read_file())
    print(count_all_arrangements(chain))
    pass

def main():
    part1()
    part2()

if __name__ == "__main__":
    sys.exit(main())
