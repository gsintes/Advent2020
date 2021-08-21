"""
Advent of code 2020 day 7
https://adventofcode.com/2020/day/7
"""

from typing import Dict, List, NamedTuple, Set

TEST_INPUT = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

TEST_INPUT2="""shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

class Bag(NamedTuple):
    color: str
    contains: Dict[str, int]

def parse_line(line: str) -> Bag:
    words = line.split()
    color = f"{words[0]} {words[1]}"
    if "no" in words:
        return Bag(color, {})
    else:
        contains = {}
        i = 4
        while i < len(words) - 1:
            if words[i].isdigit():
                number = int(words[i])
                color_child = f"{words[i + 1]} {words[i + 2]}"
                contains[color_child] = number
                i += 2
            else:
                i += 1
        return Bag(color, contains)    

def make_bags(input: str) -> List[Bag]:
    bags: List[Bag] = []
    for line in input.split("\n"):
        bags.append(parse_line(line))
    return bags

def can_contain(bag_list: List[Bag], target_color: str) -> Set[str]:
    
    parent_list: Set[str] = set()
    for bag in bag_list:
        if target_color in bag.contains.keys():
            parent_list.add(bag.color)
            parent_list = parent_list.union(can_contain(bag_list, bag.color))
    return parent_list

assert len(can_contain(make_bags(TEST_INPUT), "shiny gold")) == 4

def find_bag(bag_list: List[Bag], initial_color: str) -> Bag:
    for bag in bag_list:
        if bag.color == initial_color:
            return bag
    raise ValueError("Bag not found in the list.")


def contain_nb_bags(bag_list: List[Bag], initial_color: str) -> int:
    
    initial_bag = find_bag(bag_list, initial_color)
    if initial_bag.contains == {}:
        return 0
    else:
        contains_nb = 0
        for contained in initial_bag.contains.keys():
            contains_nb += initial_bag.contains[contained] * (1 +  contain_nb_bags(bag_list, contained))
        return contains_nb

assert contain_nb_bags(make_bags(TEST_INPUT), "shiny gold") == 32
assert contain_nb_bags(make_bags(TEST_INPUT2), "shiny gold") == 126


if __name__ == "__main__":
    file = open('input_day07.txt', mode='r')
    input = file.read()
    file.close()
    bags = make_bags(input) 
    print(len(can_contain(bags, "shiny gold")))
    print(contain_nb_bags(bags, "shiny gold"))