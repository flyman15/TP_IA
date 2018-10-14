

from Utile.utils import *
import time
import random
import chess 
import chess.svg
from IPython.core.display import SVG
from IPython.core.display import display
from IPython.display import clear_output

from Games import Game 

class ChessGame(Game):
	def __init__(self):
		self.board = chess.Board()
		self.Tab_Val_Pieces={}
		self.Tab_Val_Pieces[chess.PAWN]=1
		self.Tab_Val_Pieces[chess.KNIGHT]=3
		self.Tab_Val_Pieces[chess.BISHOP]=3
		self.Tab_Val_Pieces[chess.ROOK]=5
		self.Tab_Val_Pieces[chess.QUEEN]=10
		self.initial=self.board
		self.Partie = FIFOQueue()
		self.Partie.extend([self.initial])
		return None

	def actions(self, etat):
		"Return a list of the allowable moves at this point."
		l = [ m for m in etat.legal_moves]
		return l

	def result(self, etat, move):
		"Return the state that results from making a move from a state."
		tmp = etat.copy()
		tmp.push(move)
		return tmp

	def set_state(self, etat):
		"Return the state that results from making a move from a state."
		#self.Partie.extend([[tmp, move]])
		self.Partie.extend([etat])
		self.board= etat
		return None

	def utility(self, etat, player):
		"Return the value of this final state to player." 
		"""
		u =0
		for type_p in [chess.PAWN,chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN]:
			u += len(etat.pieces(type_p, chess.WHITE))* self.Tab_Val_Pieces[type_p]

		return (u)
		"""
		return etat.result()

	def terminal_test(self, etat):
		"Return True if this is a final state for the game."
		return self.board.is_game_over()

	def to_move(self, etat):
		"Return the player whose move it is in this state."
		return etat.turn # true si Blanc False sinon
		
	def rejoue(self, speed=2):
		l = self.Partie
		while (len(l)>0):
			e = l.pop()
			self.display(e )
			time.sleep(speed)

	def display(self, etat):
		"Print or otherwise display the state."
		#print ("display state")
		clear_output()
		display(SVG(chess.svg.board(board=etat, size =400)))
		#return None

	def display_move(self, etat, move):
		"Print or otherwise display the state."
		#print ("display state")
		clear_output()
		display(SVG(chess.svg.board(board=etat, lastmove = move, size =400)))
		#return None

	def display_old(self, etat):
		"Print or otherwise display the state."
		print (self.board)

	def __repr__(self):
		return '<%s>' % self.__class__.__name__		


