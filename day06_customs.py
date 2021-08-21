"""
Advent of code 2020 day 06
https://adventofcode.com/2020/day/6
"""
from typing import List

TEST_INPUT = """abc

a
b
c

ab
ac

a
a
a
a

b"""


def read_input(input: str) -> List[str]:
    return input.split("\n\n")

def unique_group(group_input: str) -> List[str]:
    unique_group = []
    for question in group_input:
        if question != "\n":
            if question not in unique_group:
                unique_group.append(question)
    return unique_group

def count_group(group_input: str) -> int:
    return len(unique_group(group_input))

assert count_group(read_input(TEST_INPUT)[0]) == 3
assert count_group(read_input(TEST_INPUT)[1]) == 3
assert count_group(read_input(TEST_INPUT)[2]) == 3
assert count_group(read_input(TEST_INPUT)[3]) == 1
assert count_group(read_input(TEST_INPUT)[4]) == 1

def sum_groups(inputs: List[str]) -> int:
    sum = 0
    for group_input in inputs:
        sum += count_group(group_input)
    return sum

assert sum_groups(read_input(TEST_INPUT)) == 11

def question_everyone_yes(group_input: str) -> List[str]:
    person_answers = group_input.split("\n")
    nb_pers = len(person_answers)
    answered_everyone = []
    if nb_pers == 1:
        return [char for char in person_answers[0]]

    for char in person_answers[0]:
        ok = True
        for i in range(1, nb_pers):
            if char not in person_answers[i]:
                ok = False
        if ok:
            answered_everyone.append(char)
    return answered_everyone

def count_everyone(group_input: str) -> int:
    return len(question_everyone_yes(group_input))

assert count_everyone(read_input(TEST_INPUT)[0]) == 3
assert count_everyone(read_input(TEST_INPUT)[1]) == 0
assert count_everyone(read_input(TEST_INPUT)[2]) == 1
assert count_everyone(read_input(TEST_INPUT)[3]) == 1
assert count_everyone(read_input(TEST_INPUT)[4]) == 1
assert count_everyone("""cv
v
qwvo
v""") == 1

def sum_everyone(inputs: List[str]) -> int:
    sum = 0
    for group_input in inputs:
        sum += count_everyone(group_input)
    return sum

if __name__ == "__main__":
    file = open('input_day06.txt', mode='r')
    input = file.read()
    file.close()

    print(sum_groups(read_input(input)))
    print(sum_everyone(read_input(input)))

    