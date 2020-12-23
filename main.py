import os


def get_round_winner(deck1, deck2, player_number):
    p1_card = None
    p2_card = None

    if (deck1 and deck2):
        p1_card = draw_a_card(deck1, player_number)
        p2_card = draw_a_card(deck2, player_number + 1)

    if (p1_card > p2_card):
        add_two_cards_to_deck([p1_card, p2_card], deck1)

    else:
        player_number += 1
        add_two_cards_to_deck([p2_card, p1_card], deck2)

    return player_number


def print_deck(deck, player_number):
    print(
        f'Player {player_number}\'s deck: {", ".join([str(i)for i in deck])}')


def play_game(deck1: list, deck2: list):
    round_counter = 1

    while True:
        player_number = 1

        if not len(deck1) or not len(deck2):
            break

        print(f'-- Round {round_counter} --')

        print_deck(deck1, player_number)
        print_deck(deck2, player_number + 1)

        winner = get_round_winner(deck1, deck2, player_number)

        print(f'Player {winner} wins the round!\n')
        round_counter += 1

    print_post_game(deck1, deck2, player_number)
    return round_counter


def add_two_cards_to_deck(cards, deck):
    card1, card2 = cards
    deck.extend([card1, card2])


def draw_a_card(deck, player_number):
    card = int(deck.pop(0))
    print(f'Player {player_number} plays: {card}')
    return card


def get_total(deck1: list, deck2: list):
    winner_deck = get_winner_deck(deck1, deck2)
    result = calculate_total_points(winner_deck)
    return result


def print_post_game(deck1: list, deck2: list, player_number: int):
    print('== Post-game results ==')

    print(f'Player {player_number}\'s deck: {deck1}')
    print(f'Player {player_number+1}\'s deck: {deck2}')


def calculate_total_points(deck: list):
    result = 0
    size = len(deck)

    for value in deck:
        value = int(value)
        result += value * size
        size -= 1
    return result


def get_winner_deck(deck1: list, deck2: list):
    winner_deck = []
    if (len(deck1) > len(deck2)):
        winner_deck.extend(deck1)
    else:
        winner_deck.extend(deck2)

    return winner_deck


def get_cards(path: str):
    with open(path) as f:
        game = []

        for line in f.readlines():
            line = line.replace('\n', '')
            game.extend(line.split('\n\n'))

    return game


def get_decks(cards: list):
    index = cards.index('')

    deck_p1 = cards[1:index]
    deck_p2 = cards[index + 2:]

    return [deck_p1, deck_p2]


def main():
    path = os.path.join(os.getcwd(), 'cards.txt')
    cards = get_cards(path)

    deck1, deck2 = get_decks(cards)

    total_rounds = play_game(deck1, deck2)

    total = get_total(deck1, deck2)
    print(f'The winner got {total} points!')
    print(f'{total_rounds} rounds were played during this game!')


if __name__ == "__main__":
    main()