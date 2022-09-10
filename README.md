# Chess

A chessboard, which is a checkered gameboard with 64 squares organised in an 88 grid, is used to play the two-player strategic board game of chess. People play a select few different game genres all across the world. We're going to concentrate on creating a two-player online chess game for this design challenge. The top use cases' code is provided here.

Requirements

enums, data types, and constants

Steps Required:

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
