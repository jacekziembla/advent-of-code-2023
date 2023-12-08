from dataclasses import dataclass
from enum import Enum
from collections import Counter
from typing import List

with open("07/input.txt", "r") as file:
    lines = file.read().splitlines()


def get_card_value(card: str) -> int:
    card_values = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 0,
        "T": 10
    }
    if (value := card_values.get(card)) is not None:
        return value
    return int(card)


class Figure(Enum):
    FIVE_OF_KIND = 9
    FOUR_OF_KIND = 8
    FULL_HOUSE = 7
    THREE_OF_KIND = 6
    TWO_PAIR = 5
    ONE_PAIR = 4
    HIGH_CARD = 3


def get_figure(figure_cards: List[int]) -> Figure:
    if figure_cards == [5]:
        return Figure.FIVE_OF_KIND
    if figure_cards == [4, 1]:
        return Figure.FOUR_OF_KIND
    if figure_cards == [3, 2]:
        return Figure.FULL_HOUSE
    if figure_cards == [3, 1, 1]:
        return Figure.THREE_OF_KIND
    if figure_cards == [2, 2, 1]:
        return Figure.TWO_PAIR
    if figure_cards == [2, 1, 1, 1]:
        return Figure.ONE_PAIR
    if figure_cards == [1, 1, 1, 1, 1]:
        return Figure.HIGH_CARD
    raise ValueError("Not found matching pattern")


@dataclass
class Hand:
    cards: List[str]
    bid: int
    figure: Figure = None

    def get_type(self):
        if self.figure is None:
            normal_cards = [c for c in self.cards if c != "J"]
            jokers = self.cards.count("J")
            counter = list(Counter(normal_cards).values())
            figure = sorted(counter, reverse=True)
            if jokers != 5:
                figure[0] += jokers
            else:
                figure = [5]
            self.figure = get_figure(figure)
        return self.figure

    def __eq__(self, other):
        return self.cards == other.cards

    def __lt__(self, other):
        """ First comparison by figure, second by card values """
        if self.get_type() != other.get_type():
            return self.figure.value < other.figure.value
        for i in range(len(self.cards)):
            self_value = get_card_value(self.cards[i])
            other_value = get_card_value(other.cards[i])
            if self_value != other_value:
                return self_value < other_value


hands = []
for line in lines:
    line = line.split()
    hands.append(Hand(cards=list(line[0]), bid=int(line[1])))
    # counted_cards = Counter(line[0])
    # sorted_cards = sorted(line[0], key=lambda card: (counted_cards.get(card), get_card_value(card)), reverse=True)
    # hands.append(Hand(cards=sorted_cards, bid=int(line[1])))

total_winning = 0
for index, hand in enumerate(sorted(hands)):
    rank = index + 1
    current_winning = rank * hand.bid
    total_winning += current_winning
    # print(f"Rank #{rank} | Cards={hand.cards}, {hand.figure.name}, BID={hand.bid}, WIN={current_winning}")

print(total_winning)