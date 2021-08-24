"""
Advent of code 2020 day 9
https://adventofcode.com/2020/day/9
"""

from typing import List

TEST_INPUT = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

TEST_INPUT2 = list(range(1, 26)) + [26, 53]

def is_sum_of(index: int, code_list: List[int], preamble_length: int) -> bool:
    if index <= preamble_length -1 :
        raise ValueError("Can't check for pairs in the preamble.")
    else:
        sub_list = code_list[index - preamble_length : index]
        return is_sum(code_list[index], sub_list)

def is_sum(number: int, code_list: List[int]) -> bool:
    for num1 in code_list:
        for num2 in code_list:  

            if (num1 + num2 == number) and (num1 != num2): 
                return True
    return False

assert is_sum_of(25, TEST_INPUT2, 25)
assert not is_sum_of(26, TEST_INPUT2, 25)

def find_first_not_valid(code_list: List[int], preamble_length: int) -> int:
    for index in range(preamble_length, len(code_list)):
        if not is_sum_of(index, code_list, preamble_length):
            return code_list[index]

assert find_first_not_valid([int(nb) for nb in TEST_INPUT.split("\n")], 5) == 127
assert find_first_not_valid(TEST_INPUT2, 25) == 53

def contiguous_adds_up(code_list: List[int], number: int) -> List[int]:
    for start_index in range(len(code_list)):
        res = 0
        res_list =[]
        i = start_index
        while i < len(code_list) and res < number:
            val = code_list[i]
            res_list.append(val)
            res += val
            if res == number and i != start_index:
                return res_list
            i += 1
    raise ValueError("No solution found")

assert contiguous_adds_up([int(nb) for nb in TEST_INPUT.split("\n")], 127) == [15, 25, 47, 40]


if __name__ == "__main__":
    with open('input_day09.txt') as file:
        input = [int(line) for line in file]
        print(find_first_not_valid(input, 25))
        res_list = contiguous_adds_up(input, find_first_not_valid(input, 25))
        print(min(res_list) + max(res_list))
