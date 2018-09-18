from Problems.Problems import Problem

from Chess.ChessProblems import NQueensProblem, KnightProblem, KingMaze

from Solvers.Solvers import depth_first_graph_search, breadth_first_graph_search, astar_search, best_first_graph_search

import chess


board = chess.Board("2pp4/4p2p/p3p3/3p1p2/4K2p/pp1p1pp1/7p/1p4p1  w - - 0 1")
foo = chess.B2

f = board.fen()
board.king(w)

p = KingMaze(board, foo)


print("breadth first search")
s = breadth_first_graph_search(p)
p.display_solution(s)

# p = KingMaze()





# from Problems.Problems import Problem
#
# from Chess.ChessProblems import NQueensProblem, KnightProblem, Node
#
# from Solvers.Solvers import depth_first_graph_search, breadth_first_graph_search, depth_limited_search, iterative_deepening_search, best_first_graph_search, astar_search
#
# p  = KnightProblem([0,0], [2,7])
#
# # s = depth_limited_search(p)
#
# # s = depth_first_graph_search(p)
#
# # s = iterative_deepening_search(p)
#
# print("BFS")
# s = breadth_first_graph_search(p)
#
# # """Define distance function as the square of Eucilid distance"""
# # def f(state, goal):
# #     return (state[0] - goal[0])*(state[0] - goal[0]) + (state[1] - goal[1])*(state[1] - goal[1])
# #
# #
# # s = best_first_graph_search(p, f)
# #
# p.display_solution(s)
#
#
# print("A* ")
# s = astar_search(p)
#
# p.display_solution(s)
#
#
