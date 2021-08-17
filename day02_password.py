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


def decorate_read_input(function):
    """Cette fonction va générer le décorateur."""
 
    def wrapper(input: str)-> List[Password]:
        """Voici le "vrai" décorateur.
 
        C'est ici que l'on change la fonction de base
        en rajoutant des choses avant et après.
        """
        res = []
        passwords = input.split('\n')
        for password in passwords:
            pw = password.split()
            min = int(pw[0].split('-')[0])
            max = int(pw[0].split('-')[1])
            password = function(pw[2], min, max, pw[1][0]) 
            res.append(password)
        return res
 
    return wrapper
 
 
read_input1 = decorate_read_input(Password1)
read_input2 = decorate_read_input(Password2)

def count_valid_password(input: List[Password]) -> bool:
    count = 0
    for password in input:
        if password.valid:
            count +=1
    return count

assert count_valid_password(read_input1(TEST_INPUT)) == 2
assert count_valid_password(read_input2(TEST_INPUT)) == 1

        
if __name__ == "__main__":
    # Open a file: file
    file = open('input_day02.txt',mode='r')
    # read all lines at once
    input = file.read()
    # close the file
    file.close()

    print(count_valid_password(read_input1(input)))
    print(count_valid_password(read_input2(input)))