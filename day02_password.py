"""
Advent of code 2020 day 02.
https://adventofcode.com/2020/day/2
"""
from typing import List, Text

TEST_INPUT = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""

class Password():

    def __init__(self, pw: str, letter: str) -> None:
        self.pw = pw
        self.letter = letter
        self.valid = False  

    def is_valid():
        raise NotImplementedError

class Password1(Password):

    def __init__(self, pw: str, min: int, max: int, letter: str) -> None:
        super().__init__(pw, letter)
        self.min = min
        self.max = max
        self.valid = self.is_valid()

    def is_valid(self):
        return self.min <= self.pw.count(self.letter) <= self.max

    def read_input(input: str) -> List[Password]: #TODO use a decorator for the read input function
        res = []
        passwords = input.split('\n')
        for password in passwords:
            pw = password.split()
            min = int(pw[0].split('-')[0])
            max = int(pw[0].split('-')[1])
            password = Password1(pw[2], min, max, pw[1][0]) 
            res.append(password)
        return res

class Password2(Password):
    def __init__(self, pw: str, ind1: int, ind2: int, letter: str) -> None:
        super().__init__(pw, letter)
        self.ind1 = ind1 - 1
        self.ind2 = ind2 - 1
        self.valid = self.is_valid()

    def is_valid(self) -> bool:
        v1 = (self.pw[self.ind1] == self.letter)
        v2 = (self.pw[self.ind2] == self.letter)
        return (v1 or v2) and not(v1 and v2)
    
    def read_input(input: str) -> List[Password]:
        res = []
        passwords = input.split('\n')
        for password in passwords:
            pw = password.split()
            ind1 = int(pw[0].split('-')[0])
            ind2 = int(pw[0].split('-')[1])
            password = Password2(pw[2], ind1, ind2, pw[1][0]) 
            res.append(password)
        return res



def count_valid_password(input: List[Password]) -> bool:
    count = 0
    for password in input:
        if password.valid:
            count +=1
    return count

assert count_valid_password(Password1.read_input(TEST_INPUT)) == 2
assert count_valid_password(Password2.read_input(TEST_INPUT)) == 1

        
if __name__ == "__main__":
    # Open a file: file
    file = open('input_day02.txt',mode='r')
    # read all lines at once
    input = file.read()
    # close the file
    file.close()

    print(count_valid_password(Password1.read_input(input)))
    print(count_valid_password(Password2.read_input(input)))