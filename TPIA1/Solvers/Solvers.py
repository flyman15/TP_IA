"""Search (Chapters 3-4)

The way to use this code is to subclass Problem to create a class of problems,
then create problem instances and solve them with calls to the various search
functions."""

from __future__ import generators
from Utile.utils_search import *
import math, random, sys, time, bisect, string

from Utile.utils import *
import time
import random
import chess
import chess.svg
from IPython.core.display import SVG
from IPython.core.display import display
from IPython.display import clear_output

    




#______________________________________________________________________________
## Uninformed Search algorithms


def breadth_first_graph_search(problem):
    "Search the shallowest nodes in the search tree first. [p 74]"
    return None
    
def depth_first_graph_search(problem):
    "Search the deepest nodes in the search tree first. [p 74]"
    return None

def depth_limited_search(problem, limit=50):
    return None
    
def iterative_deepening_search(problem):
    return None

#______________________________________________________________________________
# Informed (Heuristic) Search

def best_first_graph_search(problem, f):

    return None

def null_heuristic(node):
    return 0

def astar_search(problem, h=None):
    return None

