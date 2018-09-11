"""Search (Chapters 3-4)
#coding:utf-8

The way to use this code is to subclass Problem to create a class of problems,
then create problem instances and solve them with calls to the various search
functions."""

from __future__ import generators
## from Utile.utils_search import *
import math, random, sys, time, bisect, string

## from Utile.utils import *
import time
import random
from Problems.Problems import Problem as Problem

import chess
import chess.svg
from IPython.core.display import SVG
from IPython.core.display import display
from IPython.display import clear_output


class Node:
    def __init__(self):
        self.state = []
        self.parent = None


class  Knight(Problem):
    """Il s'agit d'un problème de déplacement d'un cavalier. L'échiquier
    est initialement vide, le cavalier part d'une position initiale définie dans
    le problème et doit arriver dans une case finale qui est également définie
    dans le problème, en un nombre de coups minimal. """
    def __init__(self,  start, goal, N = 8):
        self.N = N
        self.initial = Node()
        self.initial.state = [0, start[0], start[1]]
        self.goal = goal

    def  legalPosition(self, posi):
        """"To judge if the position given is a legal one"""
        if (posi[1] > -1 and posi[1] < 8 ) and  (posi[2] > -1 and posi[2] < 8 ):
            return True
        else:
            return  False

    def  successor(self,  node):
        """"For each position given, we can give 8 possible positions for the next step"""
        foo = [[1,2], [1,-2], [-1,2], [-1,-2], [2,1], [2,-1], [-2,1], [-2,-1]]
        NodeList = []
        if self.legalPosition(node.state):
            count = 0
            for e in foo:
                buf = Node()
                buf.state.append( node.state[0] + 1)
                buf.state.append(node.state[1] + e[0])
                buf.state.append(node.state[2] + e[1])
                if self.legalPosition(buf.state):
                    buf.parent = node
                    NodeList.append([count, buf])
                    count += 1
            return NodeList

    def goal_test(self, node):
        if node.state[1:3] == self.goal:
            return True
        else:
            return False

    def display_solution(self,  node):
        lis = []
        buf = node
        while buf.parent is not None:
            lis.append(buf.state)
            buf = buf.parent
        lis.append(buf.state)
        lis.reverse()
        print(lis)


class  KnightProblem(Problem):
    """Il s'agit d'un problème de déplacement d'un cavalier. L'échiquier
    est initialement vide, le cavalier part d'une position initiale définie dans
    le problème et doit arriver dans une case finale qui est également définie
    dans le problème, en un nombre de coups minimal. """
    def __init__(self,  start, goal, N = 8):
        self.N = N
        self.initial = [0, start[0], start[1]]
        self.goal = goal

    def  legalPosition(self, posi):
        """"To judge if the position given is a legal one"""
        if (posi[1] > -1 and posi[1] < 8 ) and  (posi[2] > -1 and posi[2] < 8 ):
            return True
        else:
            return  False

    def  successor(self,  state):
        """"For each position given, we can give 8 possible positions for the next step"""
        foo = [[1,2], [1,-2], [-1,2], [-1,-2], [2,1], [2,-1], [-2,1], [-2,-1]]
        posiList = []
        if self.legalPosition(state):
            count = 0
            for e in foo:
                buf = [0, 0, 0]
                buf[2] = state[2] + e[1]
                buf[1] = state[1] + e[0]
                buf[0] = state[0] + 1
                if self.legalPosition(buf):
                    posiList.append([count, buf])
                    count += 1
            return posiList

    def goal_test(self, state):
        if state[1:3] == self.goal:
            return True
        else:
            return False


    def display_solution(self, path):
        print(path)






class NQueensProblem(Problem):
    """The problem of placing N queens on an NxN board with none attacking
    each other.  A state is represented as an N-element array, where the
    a value of r in the c-th entry means there is a queen at column c,
    row r, and a value of None means that the c-th column has not been
    filled in left.  We fill in columns left to right."""

    def __init__(self, N ):
        self.N = N
        self.initial = [None] * N


    def successor(self, state): 
        "In the leftmost empty column, try all non-conflicting rows."
        if state[-1] is not None:
            return [] ## All columns filled; no successors
        else:
            def place(col, row):
                new = state[:]
                new[col] = row
                return new
            col = state.index(None)
            l= [(row, place(col, row)) for row in range(self.N)                                                                                                                                        
                     if not self.conflicted(state, row, col)]      
            return l

    def conflicted(self, state, row, col):
        "Would placing a queen at (row, col) conflict with anything?"
        for c in range(col):
            if self.conflict(row, col, state[c], c):
                return True
        return False

    def conflict(self, row1, col1, row2, col2):
        "Would putting two queens in (row1, col1) and (row2, col2) conflict?"
        return (row1 == row2 ## same row
                or col1 == col2 ## same column
                or row1-col1 == row2-col2  ## same \ diagonal
                or row1+col1 == row2+col2) ## same / diagonal

    def goal_test(self, state):
        "Check if all columns filled, no conflicts."
        if state[-1] is None: 
            return False
        for c in range(len(state)):
            if self.conflicted(state, state[c], c):
                return False
        return True

    def display_solution(self, s):
        if (self.N) !=8:
            print(s)
        else:
            state = s 
            c=[]
            for i in range(self.N):
                d=state[i]
                f=self.N-1-state[i]
                if (d>0) and (f >0):
                    c= c + [str(d)+"N"+str(f)]
                elif (d==0):
                    c= c + ["N"+str(f)]
                elif (f==0):
                    c= c + [str(d)+"N"]
            a= ( "/".join(c) + " w - - 0 1")  
            b=chess.Board(a)
            return(b)
        
         
         


