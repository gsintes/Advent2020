"""
Advent of code 2020 day 7
https://adventofcode.com/2020/day/7
"""

from typing import Dict, List, Tuple


TEST_INPUT = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

class Node:
    def __init__(self, color: str, parents: Dict["Node" : int] = {}, children: Dict["Node" : int] = {}) -> None:
        self.color = color
        self.parents = parents
        self.children = children

    def add_parent(self, bag: "Node", number: int) -> None:
        self.parents[bag] = number
    
    def add_children(self, bag: "Node", number: int) -> None:
        self.children[bag] = number
    
    def isin(self, color: str) -> Tuple[bool, "Node"]:
        for parent in self.parents.keys:
            ok, node_res = parent.isin(color)
            if ok:
                return (True, node_res)
        for child in self.children.keys:
            ok, node_res = child.isin(color)
            if ok:
                return (True, node_res)
        return (False, Node())
 

def read_input(input: str) -> List[Node]:
    connex_trees: List[Node] = []
    rules = input.split("\n")
    bags_unique = []    
    for rule in rules:
        words = rule.split()
        color_parent = f"{words[0]}  {words[1]}"
        if color_parent not in bags_unique:
            bags_unique.append(color_parent)
            parent_bag = Node(color_parent)

        if not(words[-2] == "other"):
            i = 4
            while i < len(words) - 1:
                if words[i].isdigit():
                    number = int(words[i])
                    color_bag = f"{words[i + 1]}  {words[i + 2]}"
                    if color_bag not in bags_unique:
                        bags_unique.append(color_bag)
                        child_bag = Node(color_bag, parent_bag, number)
                        parent_bag.add_children(child_bag, number)
                    i += 2
                else:
                    i += 1


if __name__ == "__main__":
    file = open('input_day07.txt', mode='r')
    input = file.read()
    file.close()

    read_input(TEST_INPUT)
