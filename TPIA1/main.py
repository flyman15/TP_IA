
from Problems.Problems import Problem

# from Chess.ChessProblems import NQueensProblem
#
# from Solvers .Solvers  import depth_first_graph_search, breadth_first_graph_search
#
# p= NQueensProblem(8)
# s = depth_first_graph_search(p)
# print(s)
# p.display_solution(s)
#
#
#
# s = breadth_first_graph_search(p)
# print(s)
# p.display_solution(s)
#


from Problems.Problems import Problem

from Chess.ChessProblems import NQueensProblem, KnightProblem

from Solvers.Solvers import depth_first_graph_search, breadth_first_graph_search, depth_limited_search, iterative_deepening_search

p  = KnightProblem([0,0], [7,7])

# s = depth_limited_search(p)

# s = depth_first_graph_search(p)

# s = iterative_deepening_search(p)

s = breadth_first_graph_search(p)

p.display_solution(s)



# p = [1,2,3,4]
# for  e in range(0,4):
#     print(p.pop())
#
# if p is None:
#     print("This is right!")
#
# if p is []:
#     print("Well done!")
#
# if len(p) == 0:
#     print("Got it!")







