# -*- coding: utf-8 -*-
from Utile.utils import *
import time
import random
import AwaleGame
from Games import Player

	
	
	
#"fonction d'evaluation pour le jeu d'awele qui est egale à la différence de nombre de graines capturées par les deux joueurs"
def feval1(game, state, depth):
    u = state.score[0] - state.score[1]   # SOUTH: 0;  NORTH: 1  
    return u


#"Strategie de diminuer le nombre de graines dans mon partie le plus vite possible"
#"Calculer seulement le nombre de graines ce qu'il y reste dans mon partie"
NORTH = 1
SOUTH = 0
def feval2(game, state, depth):
    u = sum ([state.board[x] for x in state.PITS[SOUTH]]) - sum ([state.board[x] for x in state.PITS[NORTH]]) 
    #u = state.score[0] - state.score[1]   # SOUTH: 0;  NORTH: 1  
    return u


#"Strategie Mixé"
def feval3(game, state, depth):
    u1 = state.score[0] - state.score[1]   # SOUTH: 0;  NORTH: 1 
    u2 = sum ([state.board[x] for x in state.PITS[SOUTH]]) - sum ([state.board[x] for x in state.PITS[NORTH]]) 
    u = 0.9*u1 + 0.1*u2
    return u