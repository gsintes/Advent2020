"""
Advent of code 2020 day 14
https://adventofcode.com/2020/day/14
"""

import re
from typing import List, Dict, Set

TEST_INPUT = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

REPR_LENGTH = 36

def parse_line(line: str):
    exp = re.search(r"(.+) = (.+)", line)
    if exp.group(1) == "mask":
        return (-1, list(exp.group(2)))
    mem = exp.group(1)
    exp_mem = re.search(r"^mem\[(\d+)\]", mem)
    adress = int(exp_mem.group(1))
    num = int(exp.group(2))
    return (adress, num)


def bin_to_int(bin_list: List[int]) -> int:
    binary_str = ""
    for bit in bin_list:
        binary_str += str(bit)
    return int(binary_str,2)

class Memory:
    def __init__(self) -> None:
        self.mask: List[str] = []
        self.mem: Dict[int, int] = {}
    
    def apply_line(self, line: str) -> None:
        adress, num = parse_line(line)
        if adress == -1:
            self.mask = num
        else:
            binary_num = [int(bit) for bit in bin(num).replace("0b", "")]
            missing_zeros = [0 for i in range(REPR_LENGTH - len(binary_num))]
            binary_num = missing_zeros + binary_num
            for i in range(REPR_LENGTH):
                if self.mask[i] == "1":
                    binary_num[i] = 1
                elif self.mask[i] == "0":
                    binary_num[i] = 0
            self.mem[adress] = bin_to_int(binary_num)
    
    def sum_memory(self) -> int:
        sum = 0
        for val in self.mem.values():
            sum += val
        return sum


class MemoryDecoder(Memory):
    def apply_line(self, line: str) -> None:
        adress, num = parse_line(line)
        if adress == -1:
            self.mask = num
        else:
            adresses = MemoryDecoder.get_adresses(self.mask.copy(), adress)
            for adress in adresses:
                self.mem[adress] = num

    def get_adresses(mask: List[str], adress: int) -> Set[int]:
        binary_adress = [int(bit) for bit in bin(adress).replace("0b", "")]
        missing_zeros = [0 for i in range(REPR_LENGTH - len(binary_adress))]
        binary_adress = missing_zeros + binary_adress
        copy = binary_adress.copy()
        adresses: List[int] = []
        for i in range(REPR_LENGTH):
            if mask[i] == "1":
                copy[i] = 1
            elif mask[i] == "X":
                mask[i] = 0
                copy[i] = 1
                adresses += MemoryDecoder.get_adresses(mask.copy(), bin_to_int(copy))
                copy[i] = 0
                adresses += MemoryDecoder.get_adresses(mask.copy(), bin_to_int(copy))
        if len(adresses) == 0:
            adresses.append(bin_to_int(copy))
        return set(adresses)
        

test_memory = MemoryDecoder()
for line in TEST_INPUT.split("\n"):
    test_memory.apply_line(line)
assert test_memory.sum_memory() == 208

if __name__ == "__main__":
    memory = MemoryDecoder()
    with open("input_day14.txt", "r") as file:
        for line in file:
            memory.apply_line(line)
    print(memory.sum_memory())