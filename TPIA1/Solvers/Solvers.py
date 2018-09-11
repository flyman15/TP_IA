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
    number = 0
    for e in problem.successor(problem.initial):
        fringe.append(e[1])
    while 1:
        if len(fringe) == 0:
            return False
        node = fringe.popleft()
        number += 1
        if problem.goal_test(node):
            print("Nodes explored :", number)
            return node
        for e in problem.successor(node):
            fringe.append(e[1])


def depth_first_graph_search(problem):
    "Search the deepest nodes in the search tree first. [p 74]"
    fringe = []
    number = 0
    for e in problem.successor(problem.initial):
        fringe.append(e[1])
    while(1):
        if len(fringe) == 0:
            return False
        node = fringe.pop()
        number += 1
        if problem.goal_test(node):
            print("Nodes explored :", number)
            return node
        for e in problem.successor(node):
            fringe.append(e[1])


def depth_limited_search(problem, limit=8):
    fringe = []
    number = 0
    for e in problem.successor(problem.initial):
        fringe.append(e[1])
    while 1:
        if len(fringe) == 0:
            print("Searched scale exceeded")
            return None
        else:
            node = fringe.pop()
            number += 1
            if problem.goal_test(node):
                print("Nodes explored :", number)
                return node
            if node.state[0]  != limit:
                for e in problem.successor(node):
                    fringe.append(e[1])


def iterative_deepening_search(problem, limit_start=1,  para=2, mode="plus"):
    judge = False
    limit = limit_start
    while 1:
        if judge and mode == "plus":
            limit += para
        elif judge and mode == "times":
            limit *= para
        judge = False
        fringe = []
        number = 0
        for e in problem.successor(problem.initial):
            fringe.append(e[1])
        while not judge:
            if len(fringe) == 0:
                judge = True
            else:
                node = fringe.pop()
                number += 1
                if problem.goal_test(node):
                    print("Nodes explored :", number)
                    return node
                if node.state[0] < limit:
                    for e in problem.successor(node):
                        fringe.append(e[1])


# Informed (Heuristic) Search
def best_first_graph_search(problem, f):

    return None


def null_heuristic(node):
    return 0


def astar_search(problem, h=None):
    return None

