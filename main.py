import random


movement_count = 0
bottle_len = 5


class bcolors:
    END = '\033[0m'
    RED = '\33[31m'
    GREEN = '\33[32m'
    BLUE = '\33[34m'
    PURPLE = '\33[35m'
    YELLOW = '\33[33m'
    GRAY = '\33[90m'

    colors = [RED, GREEN, BLUE, PURPLE, YELLOW, GRAY]
    colors_name = ['Vermelho', 'Verde', 'Azul', 'Roxo', 'Amarelo', 'Cinza']

    def string_colored(self, index: int) -> str:
        if index > self.colors_name.__len__():
            index = self.colors_name.__len__()
        return f'{self.colors[index]} {self.colors_name[index]} {self.END}'

    def color_name_to_index(self, name: str) -> int:
        for index, color_name in enumerate(self.colors_name):
            if color_name.lower() == name.lower():
                return index

        print('Garrafa nao encontrada')
        return -1


bg_colors = bcolors()


def mount_bottles():
    hidden_bottle = [0, 1, 2, 3, 4, 5]
    player_bottle = [0, 1, 2, 3, 4, 5]

    random.shuffle(hidden_bottle)
    random.shuffle(player_bottle)

    return hidden_bottle, player_bottle


def compare_bottles(hidden_bottle: list[int], player_bottle: list[int]) -> int:
    correct_count = 0
    for index, _ in enumerate(hidden_bottle):
        if hidden_bottle[index] == player_bottle[index]:
            correct_count += 1

    return correct_count


def print_bottles(bottle_list: list[int]):
    print('Suas garrafas:')
    for bottle in bottle_list:
        print(bg_colors.string_colored(bottle), end=' ')


def move_bottle(player_bottle: list[int], item: str, target: str):
    target_index = bg_colors.color_name_to_index(target)
    if target_index < 0:
        return

    item_index = bg_colors.color_name_to_index(item)
    if item_index < 0:
        return

    target_selected_index = player_bottle.index(target_index)
    item_selected_index = player_bottle.index(item_index)
    item_selected = player_bottle[item_selected_index]
    item_target = player_bottle[target_selected_index]
    player_bottle[target_selected_index] = item_selected
    player_bottle[item_selected_index] = item_target
    global movement_count
    movement_count += 1


def is_valid_input(item, target):

    try:
        target_int = int(target)
    except ValueError:
        return False

    if not isinstance(item, str):
        return False
    if target_int < 1 and target_int > 6:
        return False

    return True


def input_user():
    move_input = input().split(' ')
    while not is_valid_input(move_input[0], move_input[1]):
        print(
            'Para mover a Garrafa digite a cor alvo e a cor para ser alterada'
        )
        print('Exemplo: Vermelho Verde')
        print('Digite a garrafa que deseja mover e para qual posição:')
        move_input = input().split(' ')

    return move_input[0], int(move_input[1])


if __name__.__eq__("__main__"):
    hidden_bottle, player_bottle = mount_bottles()
    correct_bottles = compare_bottles(hidden_bottle, player_bottle)
    print_bottles(player_bottle)
    print(f'Total de garrafas corretas: {correct_bottles}')
    while correct_bottles < 5:
        print('Digite a garrafa que deseja mover e para qual posição:')
        item, target = input().split(' ')

        print(f'Movendo {item} para {target}')
        move_bottle(player_bottle, item, target)
        correct_bottles = compare_bottles(hidden_bottle, player_bottle)
        print_bottles(player_bottle)
        print(f'Total de garrafas corretas: {correct_bottles}')
        print('===============================================')

    print('Voce ganhou!')
    print(f'Total de movimentos: {movement_count}')
