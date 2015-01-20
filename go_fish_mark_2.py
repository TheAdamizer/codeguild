__author__ = 'Adam Van Antwerp'


"""
This version is meant to be a some-what object-oriented approach to the classic
card game 'Go-Fish'.  Decks, hands, players and the game itself will all be
objects defined by a classes.  The deck, hand and player objects will all be passed
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


# TODO: Refactor
# TODO: Reduce debug output
# TODO: Put pauses and clear screens in the console output
# TODO: Enable a custom keyword entry for hand_size during the game object instantiation
# This class creates a game object, and controls the game flow of the go-fish game.
# Most of the actual control flow happens in give_turn, fish_from_deck, determine winner, and
# get_players.
class Game:
    # Creates the local variables we need to keep track of the game state.
    def __init__(self):
        self.turn_number = 0
        self.player_list = []
        self.complete = 0
        self.deck = Deck()
        self.hand_size = 5

    # Makes a player list based on user input.
    def get_players(self):
        number_of_players = 0
        while number_of_players < 2:  # Keeps trying until the input is valid
            try:
                number_of_players = int(raw_input("Please input the number of desired players: "))
            except ValueError:        # If the user puts in something that can't be converted into an int...
                print "Invalid response."
                number_of_players = 0
        for l in range(number_of_players):
            print "Player %d..." % (l + 1)
            player_name = raw_input("Please enter your name: ")
            if player_name == '':    # It won't let any names be blank
                player_name = "Player " + str(l + 1)
                print "Defaulting to %s" % player_name
            self.player_list.append(Player(player_name))    # Creates the player objects

    # Makes sure a player has their hand full (whatever the hand_size int is set to)
    def top_off(self, player_to_top_off):
        # Won't top off if the deck is empty, for obvious reasons.
        while len(self.deck) > 0 and len(player_to_top_off.hand) < self.hand_size:
            player_to_top_off.give_card(self.deck.deal_card())  # Uses the player's give_card and deck's deal_cards

    # TODO: Make this 'empty-deck-proof', so it can be used instead of top_off inside a loop TEST THIS
    # Makes sure everyone has a hand at hand_size, and also takes care of any pairs they may get as that happens.
    def resolve_initial_pairs(self):
        for player in self.player_list:
            player.remove_pairs()
            while len(self.deck) > 0 and len(player.hand) < self.hand_size:
                self.top_off(player)
                player.remove_pairs()

    # TODO: Needs major refactoring
    # TODO: Reduce 'empty-deck-proof' redundancies
    # Manages the 'go-fish' mechanic, whereby the player has not gotten the card they want from another player, so
    # instead are recieving a card from the deck.  They should get to play again should they receive that very card
    # from the deck.
    def fish_from_deck(self, player_fishing, rank_fishing_for):
        print "Go fish!"
        pulled_card = self.deck.deal_card()        # Pulls a 'fished' card
        player_fishing.give_card(pulled_card)      # Gives the player that card cause it's theirs
        success = 0                                # We don't know if it was the right card yet...
        if pulled_card is None:                    # Deal with an empty card cause the deck is empty
            print "No cards left."
        elif rank_fishing_for == pulled_card[1]:   # If they got the right card
            print "You got it!!"
            success = 1                            # Lets us know later on to repeat their turn
            player_fishing.remove_pairs()          # Take pairs out and increment score
            while len(self.deck) > 0 and len(player_fishing.hand) < self.hand_size:    # Only top off if deck isn't
                self.top_off(player_fishing)                                           # empty and their hand is less
                player_fishing.remove_pairs()                                          # than hand_size
            print "This is your score: %d" % int(player_fishing)   # Show them their score
            return success
        print "Didn't get the card you wanted... turn over"
        player_fishing.remove_pairs()                              # Cleans up their pairs
        while len(self.deck) > 0 and len(player_fishing.hand) < self.hand_size:  # TODO: Reduce redundancy (refactor)
                self.top_off(player_fishing)
                player_fishing.remove_pairs()
        return success

    # Most of the game process happens here.  This manages the player's overall turn.  It gets input from the user
    # as far as how to proceed with their turn, then manages the trade of the card between the deck and the two players.
    # TODO: Refactoring
    # TODO: Reduce Redundancy
    def give_turn(self, player_having_turn):
        print str(player_having_turn) + ".  It's your turn."
        player_to_pick = -1                     # Opponents is a list comprehension returning the opponents of a player
        opponents = [player_.player_name for player_ in self.player_list if player_ != player_having_turn]
        print "Your valid opponents are: %s" % str(opponents)
        while player_to_pick not in opponents:  # If the user doesn't type in an opponent, asks for more input
            player_to_pick = raw_input("Please put in someone to ask a card from: ")
        opponent = None                         # Picks the user that has the same name as the 'valid' input above
        for player_ in [player_ for player_ in self.player_list if str(player_) == player_to_pick]:
            opponent = player_
        rank_to_request = ''
        print "Here is your hand: %s" % str(player_having_turn.hand)
        # This while loop keeps going as long as the user puts in a rank that's not in their hand
        while rank_to_request not in \
                [rank_ for rank_ in self.deck.ranks if player_having_turn.hand.check_for_rank(rank_)]:
            rank_to_request = raw_input("What's the card that you want?")
        result = opponent.ask_for_card(rank_to_request)  # This will return None if the opponent didn't have the rank
        go_again = 0                                     # By default the user doesn't get to go again
        if result is not None:                           # If the user got a card from the opponent
            player_having_turn.give_card(result)         # Give them the card and run remove_pairs
            player_having_turn.remove_pairs()
            while len(self.deck) != 0 and len(player_having_turn.hand) < 5:  # TODO: Reduce redundancy
                self.top_off(player_having_turn)
                player_having_turn.remove_pairs()
            print "Nice one! You got %s's card. You get to go again!" % str(opponent)
            print "Here is your score: %d" % int(player_having_turn)
            go_again = 1
        elif self.fish_from_deck(player_having_turn, rank_to_request):       # If the user successfully 'fishes'
            go_again = 1
        if len(player_having_turn.hand) == 0:            # Turn ends if their hand ends up empty (deck is empty)
            print "Hand is empty!"
            go_again = 0
        if go_again:                                     # Recursively calls this function if they get another turn
            self.give_turn(player_having_turn)
        self.resolve_initial_pairs()                     # Cleans up the pairs of all players and tops off their hands

    # This function manages the victory and outputs the results to the screen.  Allows for ties.
    def determine_winner(self):
        score_list = [player_.score for player_ in self.player_list]   # Creates a list of all the player's scores
        highest_score = max(score_list)                                # Gets the top score, even if it's a tie
        winners = []                                                   # Winner's list allows for multiple entries
        for player__ in self.player_list:
            if player__.score == highest_score:
                winners.append(player__)                               # Adds players if they're score matches the top
        if len(winners) == 1:                                          # If there is only one winner....
            print "%s wins with a score of %d!" % (str(winners[0]), highest_score)
        else:                                                          # Else, print all the winners
            print "There was a tie.  Winners are: %s" % str(winners)
            print "The winning score is: %d" % highest_score

    # This function basically runs the whole game, though most of the actual turn logic is done in other functions.
    def play(self):
        self.get_players()                          # Call get_players to make a player list
        game.resolve_initial_pairs()
        game_over = 0                               # Set end condition to false by default
        while not game_over:                        # Loop while game is still 'on'
            for player__ in self.player_list:       # Loop through the player list
                self.give_turn(player__)            # Give the player a turn, and if the hand and deck are empty...
                if len(self.deck) == 0 and 0 in [len(__player.hand) for __player in self.player_list]:
                    game_over = 1                   # Game over...
                    break                           # Break to exit the player list loop
        print "Game's over!"
        for player__ in self.player_list:           # Loops through player list to print final details...
            print "%s, your score is %d and you had a final hand of: %s" %\
                  (str(player__), int(player__), str(player__.hand))
        self.determine_winner()                     # Calls determine_winner to output winner and whatnot.
        print "Thank you for playing."

game = Game()            # Creates the game object and plays it with the play method.
game.play()
