from Utile.utils import *
import time
import random
import chess
# import ChessGame as ChessGame
from IPython.core.display import SVG
from IPython.core.display import display
from IPython.display import clear_output
from Games.Players import Player


# def feval1(game, state, depth):

# 	return (0)

# Fonction d'evaluation a utiliser pour le jeu d'echecs
# *****************************************************


def feval1(game, state, depth):
    "Return the value of this final state to player."
    u = 0
    for type_p in [chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN]:
        u += len(state.pieces(type_p, chess.WHITE)) * game.Tab_Val_Pieces[type_p]

    if depth == 0:
        v = 1
    else:
        v = -1
    # print ('legal_moves ', state.legal_moves, '=> type : ', type(state.legal_moves))
    u = u + 0.1 * len([e for e in state.legal_moves])
    return (u)
