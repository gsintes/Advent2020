"""
Advent of code 2020 dy 15
https://adventofcode.com/2020/day/15
"""

from typing import List, Dict

TEST_INPUT = [0, 3, 6]

class Game:
    def __init__(self, initial: List[int]) -> None:
        self.turn_nb = len(initial) - 1
        self.last_spoken = initial.pop()
        self.spoken: Dict[int, int] = {}
        for ind, val in enumerate(initial):
            self.spoken[val] = ind

    def __repr__(self) -> str:
        return f"turn : {self.turn_nb + 1}\nlast spoken: {self.last_spoken}\nspoken: {self.spoken}"

    def play_turn(self) -> None:
        if self.last_spoken not in self.spoken:
            self.spoken[self.last_spoken] = self.turn_nb
            self.last_spoken = 0
        else:
            ls = self.last_spoken
            self.last_spoken = self.turn_nb - self.spoken[self.last_spoken]
            self.spoken[ls] = self.turn_nb
        self.turn_nb += 1

    def play_game(self, nb_turns: int) -> int:
        while self.turn_nb < nb_turns - 1:
            self.play_turn()
        return self.last_spoken

game = Game([1, 3, 2])
assert game.play_game(2020) == 1
assert game.play_game(30000000) == 2578


if __name__ == "__main__":
    input = [15, 5, 1, 4, 7, 0]
    game = Game(input)
    print(game.play_game(2020))
    print(game.play_game(30000000))