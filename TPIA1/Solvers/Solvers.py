"""Search (Chapters 3-4)

The way to use this code is to subclass Problem to create a class of problems,
then create problem instances and solve them with calls to the various search
functions."""

from __future__ import generators
## from Utile.utils_search import *
import math, random, sys, time, bisect, string

## from Utile.utils import *
import time
import random
import chess
import chess.svg
from IPython.core.display import SVG
from IPython.core.display import display
from IPython.display import clear_output
from collections import deque


# Uninformed Search algorithms

def breadth_first_graph_search(problem):
    "Search the shallowest nodes in the search tree first. [p 74]"
    fringe = deque()
    for e in problem.successor(problem.initial):
        fringe.append(e[1])
    while 1:
        if fringe is []:
            return False
        node = fringe.popleft()
        if problem.goal_test(node):
            return node
        for e in problem.successor(node):
            fringe.append(e[1])


def depth_first_graph_search(problem):
    "Search the deepest nodes in the search tree first. [p 74]"
    fringe = []
    for e in problem.successor(problem.initial):
        fringe.append(e[1])
    while(1):
        if fringe is []:
            return False
        node = fringe.pop()
        if problem.goal_test(node):
            return node
        for e in problem.successor(node):
            fringe.append(e[1])


def depth_limited_search(problem, limit=50):
    return None


def iterative_deepening_search(problem):
    return None


# Informed (Heuristic) Search

def best_first_graph_search(problem, f):

    return None


def null_heuristic(node):
    return 0


def astar_search(problem, h=None):
    return None

