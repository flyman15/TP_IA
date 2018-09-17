from Problems.Problems import Problem

from Chess.ChessProblems import NQueensProblem, KnightProblem

from Solvers.Solvers import depth_first_graph_search, breadth_first_graph_search, astar_search, best_first_graph_search

p = KnightProblem([0, 0], [7,7])

s = astar_search(p)

print("A*")
p.display_solution(s)






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
