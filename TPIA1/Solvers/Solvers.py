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
    dejavu = []
    for e in problem.successor(problem.initial):
        fringe.append(e[1])
    dejavu.append(problem.initial.state)
    while 1:
        if len(fringe) == 0:
            return False
        node = fringe.popleft()
        print(node.state, "\n")
        number += 1
        if node.state not in dejavu:
            dejavu.append(node.state)
            if problem.goal_test(node):
                print("Nodes explored :", number)
                return node
            for e in problem.successor(node):
                if e[1].state not in dejavu:
                    fringe.append(e[1])


def depth_first_graph_search(problem):
    "Search the deepest nodes in the search tree first. [p 74]"
    fringe = []
    number = 0
    dejavu = []
    for e in problem.successor(problem.initial):
        fringe.append(e[1])
    dejavu.append(problem.initial.state)
    while(1):
        if len(fringe) == 0:
            return False
        node = fringe.pop()
        number += 1
        dejavu.append(node.state)
        if problem.goal_test(node):
            print("Nodes explored :", number)
            return node
        for e in problem.successor(node):
            if e[1].state not in dejavu:
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
            if node.depth != limit:
                for e in problem.successor(node):
                        fringe.append(e[1])


def iterative_deepening_search(problem, limit_start=1,  para=2, mode="plus"):
    judge = False
    limit = limit_start
    number = 0
    while 1:
        if judge and mode == "plus":
            limit += para
        elif judge and mode == "times":
            limit *= para
        judge = False
        fringe = []
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
                if node.depth < limit:
                    for e in problem.successor(node):
                        fringe.append(e[1])


# Informed (Heuristic) Search
def best_first_graph_search(problem, f):
    """Function defined as the  distance between the point now and the target  squared"""
    fringe = []
    number = 0
    dejavu = []
    foo = []
    for e in problem.successor(problem.initial):
        e[1].distance = f(e[1].state, problem.goal)
        foo.append(e[1])
    foo.sort(key = lambda x:  x.distance, reverse=True)
    fringe.extend(foo)
    foo.clear()
    dejavu.append(problem.initial.state)
    while(1):
        if len(fringe) == 0:
            return False
        node = fringe.pop()
        number += 1
        dejavu.append(node.state)
        if problem.goal_test(node):
            print("Nodes explored :", number)
            return node
        for e in problem.successor(node):
            if e[1].state not in dejavu:
                e[1].distance = f(e[1].state, problem.goal)
                foo.append(e[1])
        foo.sort(key=lambda x: x.distance, reverse=True)
        fringe.extend(foo)
        foo.clear()

def null_heuristic(node):
    return 0


def astar_search(problem, h=None):

    return None

