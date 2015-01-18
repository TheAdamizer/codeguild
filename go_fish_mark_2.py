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

    # Now if I call len(some deck) it will return the number of cards in the deck.
    def __len__(self):
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

    # Now it will return the length of the hand when someone calls len(the hand object).
    def __len__(self):
        return len(self.hand)


# This class creates a player object.  Much of the player class's functionality comes from wrapping the functions
# for the player's hand object.  Also, it provides ways to easily check for pairs and increment the score accordingly.
# It keeps track of the player's name as well.
class Player:

    # This creates the player object.  The player has a score and a hand object assigned to them automatically, whereas
    # the name needs to be given to the object upon instantiation.
    def __init__(self, name):
        self.player_name = name
        self.score = 0
        self.hand = Hand()
        self.opponents = []

    # This function is here to give a more direct way of increasing the user's score.  I suppose it could be used to
    # decrease it by passing a negative number.
    def increase_score(self, n):
        if type(n) is not int:
            print "What the heck?  I asked for an int!"
        else:
            self.score += n

    # This function checks to see if the player has a current card, and if they do, it takes it out of their hand
    # and returns it.  Otherwise, it returns None.
    def ask_for_card(self, rank):
        if self.hand.check_for_rank(rank):
            return self.hand.take_card(rank)
        else:
            return None

    # This function adds a card to the current players hand, like if one was returned from another player's hand. It
    # basically just wraps the hand's add_card function.
    def give_card(self, card):
        self.hand.add_card(card)

    # This function just returns the player's score
    def get_score(self):
        return self.score

    # This makes sure the textual representation of the player object is the player's name
    def __str__(self):
        return self.player_name

    # This makes sure any int typing of the object returns the score
    def __int__(self):
        return self.score

    # This uses the hand's remove_pairs function to take the pairs out of the player's hand and also increment their
    # score for the number of removed pairs.
    def remove_pairs(self):
        self.score += self.hand.remove_pairs()


class Game:
    def __init__(self):
        self.turn_number = 0
        self.player_list = []
        self.complete = 0
        self.deck = Deck()
        self.hand_size = 5

    def get_players(self):
        number_of_players = 0
        while number_of_players < 2:
            try:
                number_of_players = int(raw_input("Please input the number of desired players: "))
            except:
                print "Invalid response."
                number_of_players = 0
        for l in range(number_of_players):
            print "Player %d..." % (l + 1)
            player_name = raw_input("Please enter your name: ")
            if player_name == '':
                player_name = "Player " + str(l + 1)
                print "Defaulting to %s" % player_name
            self.player_list.append(Player(player_name))

    # def deal_hands(self):
    #     for player in self.player_list:
    #         for i in range(self.hand_size):
    #             player.give_card(self.deck.deal_card())
    #         print "%s, hand: %s" % (str(player), str(player.hand))
    #     print self.deck

    def top_off(self, player_to_top_off):
        while len(self.deck) > 0 and len(player_to_top_off.hand) < self.hand_size:
            player_to_top_off.give_card(self.deck.deal_card())

    def resolve_initial_pairs(self):
        for player in self.player_list:
            player.remove_pairs()
            while len(self.deck) > 0 and len(player.hand) < self.hand_size:
                self.top_off(player)
                player.remove_pairs()

    def fish_from_deck(self, player_fishing, rank_fishing_for):
        print "Go fish!"
        pulled_card = self.deck.deal_card()
        player_fishing.give_card(pulled_card)
        success = 0
        if pulled_card == None:
            print "No cards left."
        elif rank_fishing_for == pulled_card[1]:
            print "You got it!!"
            success = 1
            player_fishing.remove_pairs()
            while len(self.deck) > 0 and len(player_fishing.hand) < self.hand_size:
                self.top_off(player_fishing)
                player_fishing.remove_pairs()
            print "This is your score: %d" % int(player_fishing)
            return success
        print "Didn't get the card you wanted..., turn over"
        player_fishing.remove_pairs()
        while len(self.deck) > 0 and len(player_fishing.hand) < self.hand_size:
                self.top_off(player_fishing)
                player_fishing.remove_pairs()
        return success


    def give_turn(self, player_having_turn):
        print str(player_having_turn) + ".  It's your turn."
        player_to_pick = -1
        opponents = [player_.player_name for player_ in self.player_list if player_ != player_having_turn]
        print "Your valid opponents are: %s" % str(opponents)
        while player_to_pick not in opponents:
            player_to_pick = raw_input("Please put in someone to ask a card from: ")
        opponent = None
        for player_ in [player_ for player_ in self.player_list if str(player_) == player_to_pick]:
            opponent = player_
        rank_to_request = ''
        print "Here is your hand: %s" % str(player_having_turn.hand)
        while rank_to_request not in \
                [rank_ for rank_ in self.deck.ranks if player_having_turn.hand.check_for_rank(rank_)]:
            rank_to_request = raw_input("What's the card that you want?")
        result = opponent.ask_for_card(rank_to_request)
        go_again = 0
        if result != None:
            player_having_turn.give_card(result)
            player_having_turn.remove_pairs()
            while len(self.deck) != 0 and len(player_having_turn.hand) < 5:
                self.top_off(player_having_turn)
                player_having_turn.remove_pairs()
            print ("Nice one! You got %s's card. You get to go again!") % str(opponent)
            print ("Here is your score: %d") % int(player_having_turn)
            go_again = 1
        elif self.fish_from_deck(player_having_turn, rank_to_request):
            go_again = 1
        if len(self.deck) == 0:
            print "Deck is empty!"
            go_again = 0
        if go_again:
            self.give_turn(player_having_turn)
        self.resolve_initial_pairs()

    def determine_winner(self):
        score_list = [player_.score for player_ in self.player_list]
        highest_score = max(score_list)
        winners = []
        for player__ in self.player_list:
            if player__.score == highest_score:
                winners.append(player__)
        if len(winners) == 1:
            print "%s wins with a score of %d!" % (str(winners[0]), highest_score)
        else:
            print "There was a tie.  Winners are: %s" % str(winners)
            print "The winning score is: %d" % highest_score








game = Game()
game.get_players()
print game.player_list
game.resolve_initial_pairs()
game_over = 0
while not game_over:
    for player in game.player_list:
        print str(player)
        print int(player)
        print str(player.hand)
        game.give_turn(player)
        print str(player.hand)
        print "^Here is your hand at the end of the turn^"
        if len(game.deck) == 0 and 0 in [len(player_.hand) for player_ in game.player_list]:
            game_over = 1
            break
print "Game's over!"
print "Final Deck (should be empty): %s" % str(game.deck)
for player in game.player_list:
    print "%s, your score is %d and final hand of: %s" % (str(player), int(player), str(player.hand))
game.determine_winner()
print "Thank you for playing"


# wait = raw_input("press enter to continue")
# test_deck = Deck()
# hand_object_from_deal = Hand()
# # test_deck.deal_card(5)
# i = 0
# while i < 5:
#     print hand_object_from_deal.hand
#     hand_object_from_deal.add_card(test_deck.deal_card())
#     i += 1
# print hand_object_from_deal.hand
# hand_object_from_deal.add_card(('Diamond', '3'))
# print hand_object_from_deal.hand
# print hand_object_from_deal.check_for_rank('3')
# print hand_object_from_deal.check_for_rank('K')
# # taken_card = hand_object_from_deal.take_card('3')
# # print taken_card
# print hand_object_from_deal.hand
# another_hand = Hand()
# another_hand.add_card(hand_object_from_deal.take_card('3'))
# print another_hand.hand
# wait = raw_input("Waiting again")
# another_hand.add_card(('Spade', '3'))
# another_hand.add_card(('Diamond', '6'))
# score_change = another_hand.remove_pairs()
# print score_change
# print another_hand.hand
# print test_deck
# print another_hand
# print len(test_deck)
# print len(another_hand)
# test_player = Player('Adam')
# test_player.increase_score(2)
# print test_player
# print int(test_player)
# for card in hand_object_from_deal.hand:
#     test_player.give_card(card)
# print test_player.hand
# test_player.remove_pairs()
# print int(test_player)
# print test_player.hand
