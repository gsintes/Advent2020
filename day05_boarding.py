"""
Advent of code 2020 day 05
https://adventofcode.com/2020/day/5
"""
from typing import List

TEST_INPUT = """FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""

def read_input(input:str) -> List[str]:
    return input.split("\n")

def calculate_row(seat: str) -> int:
    seat = seat[:7]
    n = 0
    row = 0
    for c in seat[::-1]:
        if c == 'B':
            row += 2 ** n
        n += 1
    return row

assert calculate_row("FBFBBFFRLR") == 44
assert calculate_row("BFFFBBFRRR") == 70
assert calculate_row("FFFBBBFRRR") == 14
assert calculate_row("BBFFBBFRLL") == 102
assert calculate_row("BBFFBBBRLL") == 103

def calculate_col(seat: str) -> int:
    seat = seat[7:]
    n = 0
    col = 0
    for c in seat[::-1]:
        if c == 'R':
            col += 2 ** n
        n += 1
    return col

assert calculate_col("FBFBBFFRLR") == 5
assert calculate_col("BFFFBBFRRR") == 7
assert calculate_col("FFFBBBFRRR") == 7
assert calculate_col("BBFFBBFRLL") == 4

def seat_id(row: int, col: int) -> int:
    return row * 8 + col

def calculate_ids(seats: List[str]) -> List[int]:
    ids = []
    for seat in seats:
        ids.append(seat_id(calculate_row(seat), calculate_col(seat)))
    return ids

assert max(calculate_ids(read_input(TEST_INPUT))) == 820

def find_seat(ids: List[int]) -> int:
    ids.sort()
    for ind, seat_id in enumerate(ids):
        if ids[ind + 1] != seat_id + 1:
            return seat_id + 1

if __name__ == "__main__":
    file = open('input_day05.txt', mode='r')
    input = file.read()
    file.close()

    ids = calculate_ids(read_input(input))
    print(find_seat(ids))