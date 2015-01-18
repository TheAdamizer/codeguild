__author__ = 'Adam Van Antwerp'


"""
This version is meant to be an object-oriented approach to the classic
card game 'Go-Fish'.  Decks, hands, players and the game itself will all be
objects defined by a class.  The deck, hand and player objects will all be passed
into an instantiated game object that will handle all of the operation of the game.
"""

import random

# This class is used to create a deck object.  The deck automatically creates with all of the cards in a list.
# Each card is represented as a tuple, with the suit first and the rank second.  The values are both strings.
class Deck:
    def __init__(self):   # Creates the actual deck list that the Deck object wraps.
        self.deck = []
        self.suits = ['Spade', 'Diamond', 'Heart', 'Club']
        self.ranks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']
        for i in self.suits:
            for j in self.ranks:
                self.deck.append((i, j))

    # This automatically deals one card (a tuple) if not given any arguments.  If given an integer greater than 1, it
    # returns a list of cards.
    def deal_card(self, n=1):
        if len(self.deck) == 0:   # If the deck is empty, it complains and returns None.
            print "\n!!!!\nThere are no more cards!!!!\n!!!!!!!\n"
            return None
        if type(n) is not int:    # If it wasn't given an int it complains and returns None
            print "\n!!!!\nThis must be given an integer!!!!\n!!!!!\n"
            return None
        if n < 1:                 # If the number is less than 1 it complains and returns None.
            print "\n!!!!\nNumber of cards must be larger than 0!\n!!!!\n"
            return None
        card_to_pull = random.randint(0, len(self.deck) - 1)  # Gets an index for a random card
        card_to_pull = tuple(self.deck.pop(card_to_pull))     # Pulls a card out of the deck and assigns it
        if n == 1:
            return card_to_pull  # If that's it, it returns the card by itself.
        cards = [card_to_pull, ]
        i = 1                    # Otherwise it counts up until it has made a list of appropriate size...
        while i < n:
            print len(self.deck)
            card_to_pull = random.randint(0, len(self.deck) - 1)
            cards.append(self.deck.pop(card_to_pull))
            i += 1
        return cards             # And returns that list.

    #  This is a very simple function that returns the number of cards in the deck
    def get_deck_size(self):
        return len(self.deck)

    #  This function simply prints the current deck should someone say print <deck object>
    def __str__(self):
        return str(self.deck)


# This class is used to create the hand object.
# The hand objects contain a list of all of the cards in a player's hand.  It also contains some useful functions,
# such as checking a hand for a certain rank, removing a card of a certain rank, adding cards to the hand, and checking
# the hand for pairs and removing those pairs.
class Hand:
    # This is just making a blank hand when initialized
    def __init__(self):
        self.hand = []

    # This method adds a card to the hand, if it is a tuple that is passed as card.
    def add_card(self, card):
        if type(card) is tuple:
            self.hand.append(card)
        else:
            print "This isn't a card, dude."
    '''
    for arg in args:
                if type(arg) is list:
                    self.hand.extend(arg)
                else:
                    self.hand.append(arg)
    '''

    # This function, when given a string (hopefully a valid rank), will check to see if there are any cards of that
    # rank.  If there are, it will return True.  Otherwise it will return false.  It will complain if the hand is
    # empty.
    def check_for_rank(self, rank_to_check_for):
        current_ranks = set()    # Creates a set to contain the current ranks
        if len(self.hand) == 0:  # If the hand is actually empty...
            print "\n\n!!!!!\nThe hand is empty!\n!!!!!!\n\n"   # whine about it....
            return None                                         # and return None.
        for card in self.hand:   # Goes through every card in the hand...
            current_ranks.add(card[1])   # and adds it to a set (sets always have unique elements)
        if rank_to_check_for in current_ranks:    # If the rank we're checking for is in the current_ranks set...
            return True                           # Return True...
        return False                              # Otherwise return False.

    # This function, when given a rank, will remove ONE card of that rank from the hand and return it
    def take_card(self, rank_to_take):
        for card in self.hand:
            if card[1] == rank_to_take:
                return self.hand.pop(self.hand.index(card))

    # This function looks through the hand and removes all pairs.  It will return an int value which is the number
    # of pairs that were removed.
    def remove_pairs(self):
        pair_count = 0
        for card in self.hand:
            for card_2 in self.hand:
                if card != card_2:
                    if card[1] == card_2[1]:
                        self.hand.remove(card)
                        self.hand.remove(card_2)
                        pair_count += 1
        return pair_count

    # This function simply returns a string version of the self.hand list should someone want to print the hand object
    def __str__(self):
        return str(self.hand)

wait = raw_input("press enter to continue")
test_deck = Deck()
hand_object_from_deal = Hand()
# test_deck.deal_card(5)
i = 0
while i < 5:
    print hand_object_from_deal.hand
    hand_object_from_deal.add_card(test_deck.deal_card())
    i += 1
print hand_object_from_deal.hand
hand_object_from_deal.add_card(('Diamond', '3'))
print hand_object_from_deal.hand
print hand_object_from_deal.check_for_rank('3')
print hand_object_from_deal.check_for_rank('K')
# taken_card = hand_object_from_deal.take_card('3')
# print taken_card
print hand_object_from_deal.hand
another_hand = Hand()
another_hand.add_card(hand_object_from_deal.take_card('3'))
print another_hand.hand
wait = raw_input("Waiting again")
another_hand.add_card(('Spade', '3'))
another_hand.add_card(('Diamond', '6'))
score_change = another_hand.remove_pairs()
print score_change
print another_hand.hand
print test_deck
print another_hand