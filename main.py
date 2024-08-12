import random
from enum import Enum


class Bottles(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    PURPLE = 4
    ORANGE = 5
    PINK = 6


def mount_bottles():
    hidden_bottle = [
        Bottles.RED,
        Bottles.GREEN,
        Bottles.BLUE,
        Bottles.PURPLE,
        Bottles.ORANGE,
        Bottles.PINK,
    ]
    player_bottle = [
        Bottles.RED,
        Bottles.GREEN,
        Bottles.BLUE,
        Bottles.PURPLE,
        Bottles.ORANGE,
        Bottles.PINK,
    ]
    random.shuffle(hidden_bottle)
    random.shuffle(player_bottle)

    return hidden_bottle, player_bottle


def compare_bottles(
    hidden_bottle: list[Bottles],
    player_bottle: list[Bottles]
) -> int:
    for index, _ in enumerate(hidden_bottle):
        correct_count = 0
        if hidden_bottle[index].value == player_bottle[index].value:
            correct_count += 1

    return correct_count


if __name__.__eq__("__main__"):
    hidden_bottle, player_bottle = mount_bottles()
    correct_bottles = compare_bottles(hidden_bottle, player_bottle)
    print(correct_bottles)
