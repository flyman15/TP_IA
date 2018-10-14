from Utile.utils import *
import time
import random
from IPython.core.display import SVG
from IPython.core.display import display
from IPython.display import clear_output
from numpy import inf

from Players import Player


# ______________________________________________________________________________
# ___________________________________________________________   Players ________

class Player:

    def feval(self, state):
        "Return the value of this final state to player."
        abstract

    def best_move(self, state, game):
        "Return the player whose move it is in this state."
        abstract

    def __repr__(self):
        return '<%s>' % self.__class__.__name__


class RandomPlayer(Player):

    def feval(self, state):
        "Return the value of this final state to player."
        return 0

    def best_move(self, game, state):
        "Return the player whose move it is in this state."
        c = random.choice(game.actions(state))
        # print "Random Player move : ", c
        # game.display(state)
        return c


#  _________________________________________________________________________________

class MiniMaxplayer(Player):
    def __init__(self, depth, eval_fn):
        self.depth = depth
        self.feval = eval_fn
        self.numExplore = 0

    def best_move(self, game, state):
        def MaxValue(state, depth):
            if game.terminal_test(state) or depth is 0:
                return self.feval(game, state, 1)
            v = -inf
            for a in game.actions(state):
                self.numExplore += 1                                  
                v = max(v, MinValue(game.result(state, a), depth - 1))
            return v

        def MinValue(state, depth):
            if game.terminal_test(state) or depth is 0:
                return self.feval(game, state, 1)
            v =  inf
            for a in game.actions(state):
                self.numExplore += 1                
                v = min(v, MaxValue(game.result(state, a), depth - 1))
            return v

        foo  = []
        dep = self.depth - 1
        for a in game.actions(state):
            self.numExplore += 1
            foo.append([a, MinValue(game.result(state, a), dep)])
        c = max(foo, key = lambda x: x[1])
        return c[0]
