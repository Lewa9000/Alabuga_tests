from itertools import product


def _calculate_diversity_result(cards_a: list[str], cards_b: list[str]) -> str:
    while cards_pairs := list(
            filter(lambda cards: cards[0] == cards[1], product(cards_a, cards_b))
            ):
        for cards in cards_pairs:
            if cards[0] in cards_a and cards[1] in cards_b:
                cards_a.remove(cards[0])
                cards_b.remove(cards[1])
    else:
        return str(len(cards_a) + len(cards_b))
        

def main(input: str) -> str:
    result = []
    _, cards_a_string, cards_b_string, actions = input.split('\n', maxsplit=3)
    cards_a = cards_a_string.split(' ')
    cards_b = cards_b_string.split(' ')
    actions = actions.split('\n')
    for action in actions:
        type_, player, card = action.split(' ')
        match type_, player:
            case '1', 'A':
                cards_a.append(card)
            case '-1', 'A':
                cards_a.remove(card)
            case '1', 'B':
                cards_b.append(card)
            case '-1', 'B':
                cards_b.remove(card)
        result.append(_calculate_diversity_result(cards_a[:], cards_b[:]))
    else:
        return ' '.join(result)
