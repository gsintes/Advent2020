# pylint: disable=missing-function-docstring
"""
Advent of code 2020 day 11
https://adventofcode.com/2020/day/11
"""

from typing import List, Dict, Tuple, Callable
from collections import Counter

import numpy as np

TEST_INPUT = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

def parse_input(input: str) -> np.ndarray:
    splited_by_line = input.split("\n")
    res: List[List[str]] = []
    for line in splited_by_line:
        res.append(list(line))
    return np.array(res)

def neighbours(seats: np.ndarray, i: int, j: int) -> List[str]:
    if 0 < i < seats.shape[0] - 1:
        check_i = [-1, 0, 1]
    elif i == 0:
        check_i = [0, 1]
    elif i == seats.shape[0] - 1:
        check_i = [-1, 0]

    if 0 < j < seats.shape[1] - 1:
        check_j = [-1, 0, 1]
    elif j == 0:
        check_j = [0, 1]
    elif j == seats.shape[1] -1 :
        check_j = [-1, 0]
    neighbours = [seats[i + x, j + y] for x in check_i for y in check_j if (x, y) != (0, 0)]
    return neighbours


def find_firsts_seen_dir(seats: np.ndarray, i: int, j: int, dir: Tuple[int, int]) -> str:
    dx = dir[0]
    dy = dir[1]
    x = i + dx
    y = j + dy
    while (0 <= x < seats.shape[0]) and (0 <= y < seats.shape[1]):
        if seats[x, y] == "L":
            return "L"
        elif seats[x, y] == "#":
            return "#"
        x += dx
        y += dy
    return "."


def find_firsts_seen(seats: np.ndarray, i: int, j: int) -> List[str]:
    dirs = [
        (0, 1),
        (0, -1),
        (1, 0),
        (1, -1),
        (1, 1),
        (-1, 0),
        (-1, 1),
        (-1, -1)
    ]
    res: List[str] = []
    for direction in dirs:
        seen_dir = find_firsts_seen_dir(seats, i, j, direction)
        res.append(seen_dir)

    return res


def apply_rule(seats: np.ndarray) -> np.ndarray:
    new_seats = seats.copy()
    for i in range(seats.shape[0]):
        for j in range(seats.shape[1]):
            adjacents = neighbours(seats, i, j)
            if seats[i, j] == "L":
                if "#" not in adjacents:
                    new_seats[i , j] = "#"
            if seats[i , j] == "#":
                counter = Counter(adjacents)
                if "#" in counter.keys():
                    if counter["#"] >= 4:
                        new_seats[i, j] = "L"
    return new_seats


def rule_seen(seats: np.ndarray) -> np.ndarray:
    new_seats = seats.copy()
    for i in range(seats.shape[0]):
        for j in range(seats.shape[1]):
            seen = find_firsts_seen(seats, i, j)
            if seats[i, j] == "L":
                if "#" not in seen:
                    new_seats[i , j] = "#"
            if seats[i , j] == "#":
                counter = Counter(seen)
                if "#" in counter.keys():
                    if counter["#"] >= 5:
                        new_seats[i, j] = "L"
    return new_seats


def find_config(seats: np.ndarray, rule: Callable) ->  np.ndarray:
    old_seats = seats
    new_seats = apply_rule(old_seats)
    counter = 0
    while not (new_seats == old_seats).all():
        counter+= 1
        temp = new_seats
        new_seats = rule(new_seats)
        old_seats = temp
    return new_seats


def counter_nd(array: np.ndarray) -> Dict[str, int]:
    res: Dict[str, int] = {}
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if array[i, j] in res.keys():
                res[array[i, j]] += 1
            else:
                res[array[i, j]] = 1
    return res


def to_str(array: np.ndarray) -> str:
    res = ""
    for line in array:
        for letter in line:
            res += letter
        res += "\n"
    res = res[:-1]
    return res


TEST_SEATS = parse_input(TEST_INPUT)
assert to_str(TEST_SEATS) == TEST_INPUT
assert counter_nd(find_config(TEST_SEATS, apply_rule))["#"] == 37

STEP1RES = """#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""

STEP2RES = """#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#"""

# print(0, "\n", TEST_SEATS)
STEP1 = rule_seen(TEST_SEATS)
assert to_str(STEP1) == STEP1RES
assert to_str(rule_seen(STEP1)) == STEP2RES

assert counter_nd(find_config(TEST_SEATS, rule_seen))["#"] == 26


if __name__ == "__main__":
    file = open('input_day11.txt', mode='r')
    input = file.read()
    file.close()

    input_seats = parse_input(input)
    print(counter_nd(find_config(input_seats, apply_rule))["#"])
    print(counter_nd(find_config(input_seats, rule_seen))["#"])
