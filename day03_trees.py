"""
Advent of code 2020 day 03
https://adventofcode.com/2020/day/3
"""
from typing import List, Tuple
TEST_INPUT ="""..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

SLOPES = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1,2)
]
class Forest():
    
    def __init__(self, input: str) -> None:
        self.data: List[str] = input.split("\n")
        self.shape = (len(self.data[0]), len(self.data))


    def read(self, x: int, y: int) -> str:
        if 0 <= x < self.shape[0]:
            return self.data[y][x]
        else:
            return self.data[y][x % self.shape[0]]



TEST_FOREST = Forest(TEST_INPUT)
assert TEST_FOREST.read(0, 1) == '#'
assert TEST_FOREST.read(11, 1) == '#'
assert TEST_FOREST.read(-1, 1) == '.'
assert TEST_FOREST.read(12, 1) == '.'


def count_tree_through(forest: Forest, deltax: int, deltay: int) -> int:
    x = 0
    y = 0
    count = 0
    while y < forest.shape[1]:
        if forest.read(x, y) == "#":
            count += 1
        x += deltax
        y += deltay
    return count

assert count_tree_through(TEST_FOREST, 3, 1) == 7
assert count_tree_through(TEST_FOREST, 1, 1) == 2
assert count_tree_through(TEST_FOREST, 5, 1) == 3
assert count_tree_through(TEST_FOREST, 7, 1) == 4
assert count_tree_through(TEST_FOREST, 1, 2) == 2

def explore_slopes(forest: Forest, slopes: List[Tuple[int, int]]) -> int:
    res = 1
    for slope in slopes:
        res *= count_tree_through(forest, slope[0], slope[1])
    return res

assert explore_slopes(TEST_FOREST, SLOPES) == 336

if __name__ == "__main__":
    # Open a file: file
    file = open('input_day03.txt',mode='r')
    # read all lines at once
    input = file.read()
    # close the file
    file.close()

    print(count_tree_through(Forest(input), 3, 1))
    print(explore_slopes(Forest(input), SLOPES))
    