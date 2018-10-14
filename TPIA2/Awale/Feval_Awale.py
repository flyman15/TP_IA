
from Utile.utils import *
import time
import random
import AwaleGame
from Games import Player

	
	
	
def feval1(game, state, depth):
    u = state.score[0] - state.score[1]   # SOUTH: 0;  NORTH: 1  
    return u
