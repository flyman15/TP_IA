
from Problems.Problems import Problem

from Chess.ChessProblems import NQueensProblem

from Solvers.Solvers import depth_first_graph_search, breadth_first_graph_search

p= NQueensProblem(8)
s = depth_first_graph_search(p)
print(s)

## p.display_solution(s)
