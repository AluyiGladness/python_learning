from random import shuffle

SUITE = "H D S C". split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

mycards = [(s,r) for s in SUITE for r in RANKS]

class Deck:
    def __init__(self):
        print("creating new ordered deck of cards")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]


    def shuffle(self):
        print("shuffling cards")
        shuffle(self.allcards)

    def split_in_two(self):
        return (self.allcards[:26], self.allcards[26:])    



class Hand():
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "contains {} cards".format(len(self.cards))

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class Player():

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card))
        return drawn_card

    def remove_war_card(self):
        war_cards = []
        if len (self.hand.cards) < 3:
            return self.hand.cards
        else:

            for x in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards

    def still_has_cards(self):
        """return true if the player still has any cards  left
        """
        return len(self.hand.cards) != 0


"""
GAME LOGIC
"""

print("WELCOME TO WAR, LET'S BEGIN!")

# create new deck and split it in half
d = Deck()
d.shuffle()
half1, half2 = d.split_in_two()

# create both players
computer = Player("computer", Hand(half1))

human = input("What is your name?")
user = Player(human, Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_cards() and computer.still_has_cards():
    total_rounds += 1
    print("time for a new round")
    print("here are the current standings") 
    print(computer.name+"has a count:" +str(len(computer.hand.cards)))
    print(user.name+"has a count:" +str(len(user.hand.cards)))
    print("play a card")
    print("\n")

    table_cards = []

    c_card  = computer.play_card()
    p_card  = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)


    if c_card[1]  == p_card[1]:
        war_count += 1

        print("war!")

        table_cards.extend(user.remove_war_card())
        table_cards.extend(computer.remove_war_card())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)

        else:
            computer.hand.add(table_cards)    

    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)

        else:
            computer.hand.add(table_cards)  

print("game over, number of rounds:" +str(total_rounds))
print("a war happened " +str(war_count)+ " times")
print("Does the computer still have cards? ")
print(str(computer.still_has_cards()))
print("Does the user still have cards? ")
print(str(user.still_has_cards()))