from itertools import combinations


def _calculate_same_prefix_lenght(list_1: list[str], list_2: list[str]) -> int:
    lenght = 0
    for elem_1, elem_2 in zip(list_1, list_2):
        if elem_1 == elem_2:
            lenght += 1
        else:
            return lenght
    else:
        return lenght
        

def main(input: str) -> str:
    _, lists = input.split('\n', maxsplit=1)
    lists = lists.split('\n')[1::2]
    lenght = 0
    for list_1, list_2 in combinations(lists, 2):
        lenght += _calculate_same_prefix_lenght(list_1.split(' '), 
                                                list_2.split(' '))
    else:
        return str(lenght)
