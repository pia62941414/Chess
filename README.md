# Chess

A chessboard, which is a checkered gameboard with 64 squares organised in an 88 grid, is used to play the two-player strategic board game of chess. People play a select few different game genres all across the world. We're going to concentrate on creating a two-player online chess game for this design challenge. The top use cases' code is provided here.

System Requirements---------------------------

When creating the chess game, we'll concentrate on the following set of specifications:
Two players should be able to play chess online on the system. There will be adherence to all chess regulations worldwide. Each participant will be given a side—either black or white—at random. One move from each player will be played after the other. The initial move is made by the white side. Players are unable to undo or undo their actions. The system ought to keep track of each move made by both players. 8 pawns, 2 rooks, 2 bishops, 2 knights, 1 queen, and 1 king will be the starting pieces for each side. The game may end in one of three ways: forfeit, stalemate (a tie), or resignation from one side.

Steps Required (All files are upload seperately)--------------------

:enums, data types, and constants

:encapsulate a cell on chess board.

:encapsulate common functionality of all chess pieces.

:To encapsulate King as a chess piece.

:To encapsulate Queen as a chess piece.

:To encapsulate Knight as a chess piece.

:To encapsulate Rook as a chess piece.

:To encapsulate Bishop as a chess piece.

:To encapsulate Pawn as a chess piece.

:To encapsulate a chess move.

:To encapsulate a chess game.

:To encapsulate a chess render.

:To encapsulate a chess player.

from .render import ConsoleRender from .game import ChessGame
class Player: def play_chess(self): render = ConsoleRender() game = ChessGame(render) game.run()
if name == "main": player = Player player.play_chess()
