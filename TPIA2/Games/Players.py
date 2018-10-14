



from Utile.utils import *
import time
import random
from IPython.core.display import SVG
from IPython.core.display import display
from IPython.display import clear_output


#______________________________________________________________________________
#___________________________________________________________   Players ________

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
		c =random.choice(game.actions(state))
		#print "Random Player move : ", c
		#game.display(state)    
		return c

"""
class QueryPlayer(Player):
	
	def feval(self, state):
		"Return the value of this final state to player."
		return 0

	def best_move(self, state, game):
		"Return the player whose move it is in this state."
		print ("Query player")
		game.display(state)
		return num_or_str(raw_input('Your move? '))
"""

