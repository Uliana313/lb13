import random

class KARD:
    def __init__(self, count):
        self.count = count
        self.cards = list(range(1, count + 1))
        random.shuffle(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if self.cards:
            card = self.cards.pop()
            print(f"Видалено карту: {card}")
            return card
        else:
            print("Колода пуста!")

    def deal(self, players, cards_per_player):
        for i in range(players):
            player_cards = []
            for j in range(cards_per_player):
                card = self.draw_card()
                if card:
                    player_cards.append(card)
            print(f"Гравцю {i+1} роздано карти: {player_cards}")

deck = KARD(36)  
deck.shuffle()  
deck.draw_card()  
deck.deal(3, 6)  