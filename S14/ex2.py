# Implement standard-52 card deck in Python. Create a Card class and a Deck class.
# The cards has to be printable ex:
# print(card)
# >>> 5
# The deck must keep a list of cards inside it. Put de cards in deck at instantation,
# 52 cards, no duplicates. The deck must implement get_cards(number).
#




class Card:
    
    def __init__(self, number, symbol):
        self.number = number
        self.symbol = symbol

    def __str__(self):
        return self.number + self.symbol

    def __repr__(self):
        return self.__str__()



class Deck:

    def __init__(self):
        self.__AVAILABLE_SYMBOLS = ("♠", "♥", "♦", "♣")
        self.__cards = []
        self.__generate_cards()

    def get_cards(self, number):
        r_cards = []
        for i in range(number):
            r_cards.append(self.__cards.pop())
        return r_cards
            
    def shuffle(self):
        pass

    def generate_available_numbers(self):
        a_n = []
        for i in range(2, 11):
            a_n.append(str(i))
        a_n.extend(["J", "Q", "K", "A"])
        return a_n

    def __generate_cards(self):
        for i in self.generate_available_numbers():
            for j in self.__AVAILABLE_SYMBOLS:
                self.__cards.append(Card(i, j))

    def get_all_cards(self):
        return self.get_cards(52)

deck = Deck()

print(deck.get_all_cards())

