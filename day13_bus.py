"""
Advent of code 2020 day 13
https://adventofcode.com/2020/day/13
"""

from typing import Dict, Tuple, List

TEST_INPUT = """939
7,13,x,x,59,x,31,19"""

def parse_input(input: str) -> Tuple[int, List[int]]:
    lines = input.split("\n")
    earliest_time = int(lines[0])
    bus = [int(val) for val in lines[1].split(",") if val.isdigit()]
    return (earliest_time, bus)

def first_passages(first_time: int, buses: List[int]) -> List[int]:
    res: List[int] = []
    for bus in buses:
        res.append(bus * (1 + first_time // bus))
    return res

test_time = parse_input(TEST_INPUT)[0]
test_bus = parse_input(TEST_INPUT)[1]

def bus_to_take(first_time: int, buses: List[int]) -> int:
    first_p = first_passages(first_time, buses)
    return buses[first_p.index(min(first_p))]

def time_to_wait(first_time: int, buses: List[int]) -> int:
    first_p = first_passages(first_time, buses)
    return min(first_p) - first_time

assert time_to_wait(test_time, test_bus) == 5
assert bus_to_take(test_time, test_bus) == 59


## part 2
def read_instruction(input: str) -> Dict[int, int]:
    instructions : Dict[int, int]= {}
    for ind, inst in enumerate(input.split("\n")[1].split(",")):
        if inst.isdigit():
            instructions[int(inst)] = (int(inst) - ind) % int(inst)

    return instructions

def find_time(instructions: Dict[int, int]) -> int:
    keys = sorted(instructions.keys(), reverse=True)
    i = instructions[keys[0]]
    incr = keys[0]
    for key in keys[1:]:
        while i % key != instructions[key]:
            i += incr
        incr *= key
    return i 

test_instructions = read_instruction(TEST_INPUT)
assert find_time(test_instructions) == 1068781
assert find_time({17: 0, 13: 11, 19: 16}) == 3417
assert find_time({1789: 0, 37: 36, 47: 45, 1889: 1886}) == 1202161486

if __name__ == "__main__":
    file = open('input_day13.txt', mode='r')
    input = file.read()
    file.close()

    time = parse_input(input)[0]
    buses = parse_input(input)[1]
    print(time_to_wait(time, buses) * bus_to_take(time, buses))

    print(find_time(read_instruction(input)))