"""Games, or Adversarial Search. (Chapter 5)
"""

from Utile.utils import *
import time
import random
from IPython.core.display import SVG
from IPython.core.display import display
from IPython.display import clear_output


# from Games.AlphaBetaPlayer import ABplayer
# from Games.Players import RandomPlayer #, QueryPlayer


def play_game(game,coup, *players):
    """Play an n-person, move-alternating game.
    >>> play_game(Fig52Game(), alphabeta_player, alphabeta_player)
    3
    """
    state = game.initial
    game.display(state)
    i = 1
    while True and (i < coup):
        # print ("iteration ", i, " game : ", game.board)
        i += 1
        print(i)
        # print ("nouveau coup")
        for player in players:
            move = player.best_move(game, state)
            # print (move)
            state = game.result(state, move)
            game.set_state(state)
            # print ("disolay")
            # game.display_move(state, move)
            game.display(state)
            # Wait for 5 seconds
            time.sleep(1)
            if game.terminal_test(state):
                # game.display(state)
                # print(state.result())
                print ("fin de partie")
                # print(i)
                return [state.result(), game.utility(state, game.to_move(game.initial))]


# ______________________________________________________________________________
# Some Sample Games

class Game:
    """A game is similar to a problem, but it has a utility for each
    state and a terminal test instead of a path cost and a goal
    test. To create a game, subclass this class and implement actions,
    result, utility, and terminal_test. You may override display and
    successors or you can inherit their default methods. You will also
    need to set the .initial attribute to the initial state; this can
    be done in the constructor."""

    def actions(self, state):
        "Return a list of the allowable moves at this point."
        abstract

    def result(self, state, move):
        "Return the state that results from making a move from a state."
        abstract

    def utility(self, state, player):
        "Return the value of this final state to player."
        abstract

    def terminal_test(self, state):
        "Return True if this is a final state for the game."
        return not self.actions(state)

    def to_move(self, state):
        "Return the player whose move it is in this state."
        return state.to_move

    def display(self, state):
        "Print or otherwise display the state."
        print state

    def __repr__(self):
        return '<%s>' % self.__class__.__name__
