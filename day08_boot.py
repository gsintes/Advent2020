""""
Advent of code 2020 day 08
https://adventofcode.com/2020/day/8
"""

from typing import List, NamedTuple, Set

TEST_INPUT = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

class Instruction(NamedTuple):
    inst: str
    num: int

class Program:
    def __init__(self, code: List[Instruction]) -> None:
        self.code = code
        self.index = 0
        self.count_steps = 0
        self.accumulator = 0
        self.visited: Set[int] = set()
        self.looped = False

    def __repr__(self) -> str:
        return repr(self.code)

    def take_step(self) -> None:
        self.count_steps += 1
        self.visited.add(self.index)
        if len(self.visited) != self.count_steps:
            self.looped = True
        else:
            inst = self.code[self.index].inst
            num = self.code[self.index].num
            if inst == "nop":
                self.index += 1
            elif inst == "acc":
                self.accumulator += num
                self.index += 1
            elif inst == "jmp":
                self.index += num
            else:
                raise ValueError("Not accepted instruction")

    def run_code(self) -> None:
        while not self.looped and self.index < len(self.code):
            self.take_step()


def parse_line(line: str) -> Instruction:
    splitted = line.split()
    return Instruction(splitted[0], int(splitted[1]))



def read_input(input:str) -> List[Instruction]:
    intructions: List[Instruction] = []
    for line in input.split("\n"):
        intructions.append(parse_line(line))
    return intructions

# Test
program = Program(read_input(TEST_INPUT))
program.run_code()
assert program.accumulator == 5

def correct_code(program: List[Instruction]) -> Program:
    for ind, instruction in enumerate(program):
        copy = program.copy()
        if instruction.inst == "nop":
            copy[ind] = Instruction("jmp", instruction.num)
            prog = Program(copy)
            prog.run_code()
            if not prog.looped :
                return prog 
        elif instruction.inst == "jmp":
            copy[ind] = Instruction("nop", instruction.num)
            prog = Program(copy)
            prog.run_code()
            if not prog.looped :
                return prog 
    raise ValueError("Not correctible in one change")

# Test
list_input = read_input(TEST_INPUT)
corrected = correct_code(list_input)

assert corrected.accumulator == 8

if __name__ == "__main__":
    file = open('input_day08.txt', mode='r')
    input = file.read()
    file.close()

    list_input = read_input(input)
    program = Program(list_input)
    program.run_code()
    print(program.accumulator)
 
    
    corrected = correct_code(list_input)    

    print(corrected.accumulator)