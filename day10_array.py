"""
Advent of code 2020 day 10
https://adventofcode.com/2020/day/10
"""

from typing import Dict, List

TEST_INPUT = """16
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

TEST_INPUT2 = """28
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

LIST_TEST1 = [int(nb) for nb in TEST_INPUT.split("\n")]
LIST_TEST2 = [int(nb) for nb in TEST_INPUT2.split("\n")]

def build_chain(adapters: List[int]) -> List[int]:
    adapters.sort()
    return adapters

def differences(chain: List[int]) -> List[int]:
    diff = [chain[0]]
    for i in range(len(chain) - 1):
        diff.append(chain[i + 1] - chain[i])
    diff.append(3)
    return diff

def count_diff(differences: List[int]) -> Dict[int, int]:
    counter: Dict[int, int] = {}
    for diff in differences:
        if diff not in counter.keys():
            counter[diff] = 1
        else:
            counter[diff] += 1
    return counter


assert count_diff(differences(build_chain(LIST_TEST1))) == {1: 7, 3: 5}
assert count_diff(differences(build_chain(LIST_TEST2))) == {1: 22, 3: 10}

def number_ways(adapters: List[int]) -> int:
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters_set = set(adapters)
    output = adapters[-1]
    # nb_ways[i] is the nb of ways to go to i
    nb_ways = [0] * (output + 1)
    # Initialization
    nb_ways[0] = 1
    if 1 in adapters_set:
        nb_ways[1] = 1
    if 2 in adapters_set:
        if 1 in adapters_set:
            nb_ways[2] = 2
        else:
            nb_ways[2] = 2

    for i in range(3, output + 1):
        if i not in adapters_set:
            continue
        nb_ways[i] = nb_ways[i - 1] + nb_ways[i - 2] + nb_ways[i - 3] 
    return nb_ways[output]

    
assert number_ways(LIST_TEST1) == 8
assert number_ways(LIST_TEST2) == 19208


if __name__ == "__main__":
    with open('input_day10.txt') as file:
        adapters = [int(line) for line in file]
        dict_diff = count_diff(differences(build_chain(adapters)))
        print(number_ways(adapters))