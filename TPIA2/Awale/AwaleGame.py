PIT_COUNT = 6
PEBBLE_COUNT = 4
NORTH = 1
SOUTH = 0
EQUALITY = 2
NOT_ENDED  = -1

GAME_NO_WINNER = -1
GAME_CONTINUE = -2

"""Games, or Adversarial Search. (Chapter 5)
"""

from Utile.utils import *
import time
import random
import sys
import numpy as np
import copy

import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow 

from IPython.core.display import SVG
from IPython.core.display import display
from IPython.display import clear_output

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

from Games import Game 
             
class AwaleGame(Game):
	
	def __init__(self, board = None):
	
		if (board==None):
			self.board = Board(size=PIT_COUNT)
		else:
			self.board = Board(size=PIT_COUNT, board = board)
		#print(render(board))
		"""
		players = [
			get_complement_properties_player(0, player_one),
			get_complement_properties_player(1, player_two)
		  ]
		"""  
		self.initial = self.board
		self.Partie = FIFOQueue()
		self.Partie.extend([self.initial])
		return None

	def actions(self, state):
		"Return a list of the allowable moves at this point."
		l = [ m for m in state.legal_moves]
		return l

	def result(self, state, move):
		"Return the state that results from making a move from a state."
		tmp = state.copy()
		tmp.push(move)
		return tmp

	def set_state(self, state):
		"Return the state that results from making a move from a state."
		self.board= state
		self.Partie.extend([state])
		return None

	def utility(self, state, player):
		"Return the value of this final state to player." 
		"""
		u =0
		for type_p in [chess.PAWN,chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN]:
			u += len(etat.pieces(type_p, chess.WHITE))* self.Tab_Val_Pieces[type_p]

		return (u)
		"""
		return state.result()

	def terminal_test(self, etat):
		"Return True if this is a final state for the game."
		return self.board.is_game_over()

	def to_move(self, state):
		"Return the player whose move it is in this state."
		return state.turn # true si Blanc False sinon
			
	def rejoue(self, speed=2):
		l = self.Partie
		while (len(l)>0):
			e = l.pop()
			self.display(e )
			time.sleep(speed)	

	def display(self, state):
		"Print or otherwise display the state."
		#print ("display state")
		clear_output()
		state.display()
		#display(SVG(chess.svg.board(board=self.board, size =200)))
		#return None

	def display_move(self, state, move):
		"Print or otherwise display the state."
		#print ("display state")
		clear_output()
		#display(SVG(chess.svg.board(board=self.board, lastmove = move, size =400)))
		#return None
		
	def display_old(self, state):
		"Print or otherwise display the state."
		state.display()

	def __repr__(self):
		return '<%s>' % self.__class__.__name__		

class Board:
	def __init__(self, size=6, board=None):
		# Create a new board, simple array
		self.size = size
		if (board==None):
			self.board = [PEBBLE_COUNT] * size *2
		else:
			self.board = board
		self.PITS = [range(0,size), range(size, 2*size)]
		self.turn = SOUTH
		self.legal_moves = self.PITS[self.turn]
		self.score = [0,0]
		self.init_display()
		return None
		
	def result(self):
		if (self.score[NORTH]> 24):
			return NORTH
		elif (self.score[SOUTH] > 24):
			return SOUTH
		elif ((self.score[SOUTH]==self.score[NORTH]) and (self.score[NORTH]==24)):
			return EQUALITY
		elif (self.legal_moves ==[]):
			self.deal_position()
			return -3  ## to be changed
		else:
			return NOT_ENDED
	
	def is_game_over(self):

		return (self.result() != NOT_ENDED)
		
	def change_turn(self):
		if (self.turn==NORTH):
			self.turn = SOUTH
		else:
			self.turn = NORTH
		return None
				
	def push(self, move):
		# starving est une fonction, qui doit modifier les coups leagaux
		# can_feed est un truc ateser si starving et qui conditionne la fin de partie ou pas.

		"""
		if self.must_feed():
			self.select_feeding_moves_only()
			if (self.legal_moves == []):
				self.deal_position(move)
				return None
		else:
		"""
			
		self.execute(move)

		self.change_turn()
		#print ('turn ' , self.turn)
		#print ( ' PITS ', self.PITS, ' New PITS ', self.PITS[self.turn])		
		self.legal_moves = self.PITS[self.turn]
		self.legal_moves = [move for move in self.legal_moves if self.can_play(move) ] 
		if self.must_feed():
			self.select_feeding_moves_only()
		if (self.legal_moves==[]):
			self.deal_position()
		return None
		
	def must_feed(self):
		if (self.turn==NORTH):
			return (sum ([self.board[x] for x in self.PITS[SOUTH]]) ==0)
		else:
			return (sum ([self.board[x] for x in self.PITS[NORTH]]) ==0)
	
	def feed(self, move):
		nb_peebles_to_distribute = self.board[move]
		if (nb_peebles_to_distribute > self.size):
			return True
		else:
			if (move in self.PITS[SOUTH]):
				return (nb_peebles_to_distribute> self.size-move)
			else:
				return (2*self.size - move -1 < nb_peebles_to_distribute)
	
	def select_feeding_moves_only(self):
		self.legal_moves = [move for move in self.legal_moves if self.feed(move)]
		return None
		
		
	def copy(self):		
		return  copy.deepcopy(self)
		
	def can_play(self, move):
		
		is_empty_pit = (self.board[move] == 0)
		move_possible = (move in self.legal_moves)  and (not is_empty_pit) and (not self.will_starve(move))
		return move_possible

	def deal_position(self):
		"""
		seeds = board[position]
		board[position] = 0
		i = position

		while seeds > 0:
			i += 1
			if i % PIT_COUNT != position:
				board[i % PIT_COUNT] += 1
				seeds -= 1

		return i % PIT_COUNT, board
		"""
		#if (self.turn==NORTH):
		self.score[0]+= (sum ([self.board[x] for x in self.PITS[SOUTH]]))
		#else:
		self.score[1]+= (sum ([self.board[x] for x in self.PITS[NORTH]]))
		return None		
		
	def next_position(self, start_position, position):

		if (position < self.size-1):
			return position +1
		elif (position < 2*self.size -1):
			return position +1
		else:
			return 0

	def previous_position(self, position):

		if (position > 0):
			return position -1
		elif (position > self.size ):
			return position +1
		else:
			return self.size*2 -1			
			
	def execute(self, start_position):

		def adversary_position(start_position, position):
			#if (position not in self.PITS[self.turn])
			return ((position - self.size) * (start_position - self.size) <0) or ((position +1 - self.size) * (start_position +1 - self.size)<0)

		def is_prise_possible(tstart_position, position):
			return (adversary_position(start_position, position)) and ((self.board[position] >=2) and (self.board[position] <=3))		

			
		def prise(start_position, position):
			if (is_prise_possible(start_position, position)):
				captured = self.board[position]
				self.board[position]=0
				#print 'prise possible'
				return captured
			else:
				#print 'prise impossible', position, self.board[position], adversary_position(start_position, position), is_prise_possible(position)
				return 0

		def distrib(start_position, position):
			self.board[position] +=1
			next_pos = self.next_position(start_position, position)
			if (start_position == next_pos):
				next_pos = self.next_position(start_position, next_pos)
			return next_pos

		####___________ Execute un coup ___________
		
		#print 'dans execute'
		captured_peebles = 0
		nb_peebles_to_distribute = self.board[start_position]
		self.board[start_position]=0
		position = self.next_position(start_position, start_position)

		while (nb_peebles_to_distribute>0):		
			position = distrib(start_position, position)
			nb_peebles_to_distribute -=1
			
		position = self.previous_position(position)
		position_finale = position

		i=0
		while (is_prise_possible(start_position, position)):
			position = self.previous_position(position)
			i +=1	
			
		if (i >4):
			return None	
		else:	
			position = position_finale
			capture = prise(start_position, position)
			#print ('capture', capture)
			i=0
			while (capture>0) and (i<4):
				position = self.previous_position(position)
				captured_peebles += capture
				capture = prise(start_position, position)
				i +=1	
			self.score [self.turn] += captured_peebles

		return None

	def will_starve(self,move):
		return False
		
	def can_feed(self):
		return True

	def display_text(self):
			
		def display_board_top(board, half):
			# Display with index
			render_str = ''
			for i in range(2*half-1, half-1, -1):
				render_str += '\t' + str(i) + ' [' + str(board[i]) + ']'
			return render_str


		def display_board_bottom(board, half):
			# Display with index
			render_str = ''
			for i in range(0, half):
				render_str += '\t' + str(i) + ' [' + str(board[i]) + ']'
			return render_str
			
		def render_score(score):
			score_str = "Score:\t South: {}\t North: {}\n"
			return score_str.format(score[0], score[1])

		render_str = ''
		half = int(len(self.board) / 2)
		render_str += '\n'
		# Board top
		render_str += display_board_top(self.board, half)
		render_str += '\n'
		# Board bottom
		render_str += display_board_bottom(self.board, half)
		render_str += '\n'
		
		print render_str
		print (render_score(self.score))
		return None

	def display_text2(self, move):
			
		def display_board_top(board, half):
			# Display with index
			render_str = ''
			for i in range(2*half-1, half-1, -1):
				render_str += '\t' + ' [' + str(board[i]) + ']'
			return render_str


		def display_board_bottom(board, half):
			# Display with index
			render_str = ''
			for i in range(0, half):
				render_str += '\t' + ' [' + str(board[i]) + ']'
			return render_str
			
		def render_score(score):
			score_str = "Score:\t South: {}\t North: {}\n"
			return score_str.format(score[0], score[1])

		render_str = ''
		half = int(len(self.board) / 2)
		render_str += '\n'
		# Board top
		render_str += display_board_top(self.board, half)
		render_str += '\n'
		# Board bottom
		render_str += display_board_bottom(self.board, half)
		render_str += '\n'
		
		print render_str
		print (render_score(self.score))
		return None
		
	def init_display(self):
		self.img = Image.open("awaleplateau.jpg")
		self.i=1
		#font = ImageFont.truetype("abel/abel-regular.ttf", 64)
		return None
		
	def display(self):
		#img = Image.open("awaleplateau.jpg")
		#draw = self.draw    # ImageDraw.Draw(img)
		#font = ImageFont.truetype(<font-file>, <font-size>)
		##### clear_output()
		img= copy.copy(self.img)
		#img
		font = ImageFont.truetype("abel/abel-regular.ttf", 64)
		draw = ImageDraw.Draw(img)

		clear_output()
		Coordinates1 = [(230  + i* 140, 420) for i in range(6)]
		Coordinates2 = [(230  + i* 140, 280) for i in range(6)]
		Coordinates2.reverse()
		#Coordinates = Coordinates1 + Coordinates2
		for i in range(len(Coordinates1)):
			c = Coordinates1[i]
			draw.text(c,str(self.board[i]),(255,255,255),font=font)

		for i in range(len(Coordinates2)):
			c = Coordinates2[i]
			draw.text(c,str(self.board[i+self.size]),(255,255,255),font=font) 
		
		draw.text((100,350), str(self.score[0]),(255,255,255),font=font) 
		draw.text((1060,350), str(self.score[1]),(255,255,255),font=font) 
		#display(imshow(np.asarray(img)) )
		#plt.close()
		plt.figure()
		self.i +=1
		#plt.imshow(np.asarray(img))
		#plt.close()
		#### img.show()
		plt.imshow(img)
		#plt.close()
		#sys.stdout.flush()
		#display(img)
		#imshow(np.asarray(img))
		#time.sleep(30)
		return None

	
		
		
		
