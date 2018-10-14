from Games import Game, play_game

from Chess import ChessGame
from Chess.Feval_Chess import feval1

from Games.Players import RandomPlayer
from Games.AlphaBetaPlayer import MiniMaxplayer

# j = ChessGame()
# a = play_game(j, p = MiniMaxplayer(depth=3, eval_fn=feval1), RandomPlayer() )

foo = []
for i in range(1,5):
    j = ChessGame()
    p = MiniMaxplayer(depth=i, eval_fn=feval1)
    a = play_game(j, p, RandomPlayer() )
    foo.append(p.numExplore)

from matplotlib.pyplot import plot
plot(range(1,5), foo)    