import random


bottle_colors = ['Vermelho', 'Verde', 'Azul', 'Roxo', 'Laranja', 'Rosa']


def bottle_color(index: int):
    if index > bottle_colors.__len__():
        return bottle_colors[0]
    return bottle_colors[index]


def mount_bottles():
    hidden_bottle = [0, 1, 2, 3, 4, 5]
    player_bottle = [0, 1, 2, 3, 4, 5]

    random.shuffle(hidden_bottle)
    random.shuffle(player_bottle)

    return hidden_bottle, player_bottle


def compare_bottles(hidden_bottle: list[int], player_bottle: list[int]) -> int:
    for index, _ in enumerate(hidden_bottle):
        correct_count = 0
        if hidden_bottle[index] == player_bottle[index]:
            correct_count += 1

    return correct_count


def print_bottles(bottle_list: list[int]):
    for bottle in bottle_list:
        print(bottle_color(bottle))


if __name__.__eq__("__main__"):
    hidden_bottle, player_bottle = mount_bottles()
    correct_bottles = compare_bottles(hidden_bottle, player_bottle)
    print_bottles(player_bottle)
    print(f'Total de garrafas corretas: {correct_bottles}')
