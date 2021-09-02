"""
Advent of code 2020 day 12
https://adventofcode.com/2020/day/12
"""

from day04_passport import INVALID_TEST
import re
from typing import DefaultDict, NamedTuple, List
import math

TEST_INPUT = """F10
N3
F7
R90
F11"""

class Instruction(NamedTuple):
    direction: str
    distance: int

def parse_line(line: str) -> Instruction:
    exp = re.search(r"([F L R N E W S])(\d+)", line)
    direction = exp.group(1)
    distance = int(exp.group(2))
    return Instruction(direction, distance)

TEST_INSTRUCTION: List[Instruction] = [parse_line(line) for line in TEST_INPUT.split("\n")]

class Boat:
    def __init__(self) -> None:
        # N/S coord
        self.x = 0 
        # E/W coord
        self.y = 0
        self.facing: List[int, int] = [0, 1]
    
    def __repr__(self) -> str:
        return f"x: {self.x}, y: {self.y}, facing: {self.facing}"

    def run_instruction(self, instruction: Instruction) -> None:
        if instruction.direction == "N":
            self.x += instruction.distance
        elif instruction.direction == "S":
            self.x -= instruction.distance
        elif instruction.direction == "E":
            self.y += instruction.distance
        elif instruction.direction == "W":
            self.y -= instruction.distance
        
        elif instruction.direction == "F":
            self.x += self.facing[0] * instruction.distance
            self.y += self.facing[1] * instruction.distance
        elif instruction.direction == "R":
            cos = round(math.cos(math.radians(instruction.distance)))
            sin = round(math.sin(math.radians(instruction.distance)))
            facing = self.facing.copy()
            self.facing[0] =  cos * facing[0] - sin * facing[1]
            self.facing[1] = sin * facing[0] + cos * facing[1]
        elif instruction.direction == "L":
            cos =  round(math.cos(- math.radians(instruction.distance)))
            sin =  round(math.sin(- math.radians(instruction.distance)))
            facing = self.facing.copy()
            self.facing[0] =  cos * facing[0] - sin * facing[1]
            self.facing[1] = sin * facing[0] + cos * facing[1]

    def distance(self) -> int:
        return abs(self.x) + abs(self.y)
    
    def run_instructions(self, instructions: List[Instruction]) -> None:
        for instruction in instructions:
            self.run_instruction(instruction)
    

class WaypointBoat(Boat):
    def __init__(self) -> None:
        super().__init__()
        self.waypoint: List[int, int] = [1, 10]
    
    def __repr__(self) -> str:
        return f"x: {self.x}, y: {self.y}, waypoint: {self.waypoint}" 

    def run_instruction(self, instruction: Instruction) -> None:
        if instruction.direction == "N":
            self.waypoint[0] += instruction.distance
        elif instruction.direction == "S":
            self.waypoint[0] -= instruction.distance
        elif instruction.direction == "E":
            self.waypoint[1] += instruction.distance
        elif instruction.direction == "W":
            self.waypoint[1] -= instruction.distance
        
        elif instruction.direction == "F":
            self.x += self.waypoint[0] * instruction.distance
            self.y += self.waypoint[1] * instruction.distance
        elif instruction.direction == "R":
            cos = round(math.cos(math.radians(instruction.distance)))
            sin = round(math.sin(math.radians(instruction.distance)))
            waypoint = self.waypoint.copy()
            self.waypoint[0] =  cos * waypoint[0] - sin * waypoint[1]
            self.waypoint[1] = sin * waypoint[0] + cos * waypoint[1]
        elif instruction.direction == "L":
            cos =  round(math.cos(- math.radians(instruction.distance)))
            sin =  round(math.sin(- math.radians(instruction.distance)))
            waypoint = self.waypoint.copy()
            self.waypoint[0] =  cos * waypoint[0] - sin * waypoint[1]
            self.waypoint[1] = sin * waypoint[0] + cos * waypoint[1]



test_boat = Boat()
test_boat.run_instructions(TEST_INSTRUCTION)
assert test_boat.distance() == 25

test_waypoint_boat = WaypointBoat()
test_waypoint_boat.run_instructions(TEST_INSTRUCTION)
assert test_waypoint_boat.distance() == 286


if __name__ == "__main__":
    with open("input_day12.txt", "r") as file:
        instructions = [parse_line(line) for line in file if line != ""]
        boat = Boat()
        boat.run_instructions(instructions)
        print(boat.distance())

        boat = WaypointBoat()
        boat.run_instructions(instructions)
        print(boat.distance())