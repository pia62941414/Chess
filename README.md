# Chess (Hitwicket Assignment)

A chessboard, which is a checkered gameboard with 64 squares organised in an 88 grid, is used to play the two-player strategic board game of chess. People play a select few different game genres all across the world. We're going to concentrate on creating a two-player online chess game for this design challenge. The top use cases' code is provided here.

System Requirements---------------------------

When creating the chess game, we'll concentrate on the following set of specifications:
Two players should be able to play chess online on the system. There will be adherence to all chess regulations worldwide. Each participant will be given a side—either black or white—at random. One move from each player will be played after the other. The initial move is made by the white side. Players are unable to undo or undo their actions. The system ought to keep track of each move made by both players. 8 pawns, 2 rooks, 2 bishops, 2 knights, 1 queen, and 1 king will be the starting pieces for each side. The game may end in one of three ways: forfeit, stalemate (a tie), or resignation from one side.

Steps Required (All files are upload seperately)--------------------

## :enums, data types, and constants

 from copy import deepcopy from .pieces import Piece, PieceFactory from .moves import ChessPosition, MoveCommand from .constants import CHESS_BOARD_SIZE, INITIAL_PIECE_SET_SINGLE, PieceType

 class ChessBoard: def init(self, size=CHESS_BOARD_SIZE): self._size = size self._pieces = [] self._white_king_position = None self._black_king_position = None self._initialize_pieces(INITIAL_PIECE_SET_SINGLE)

## :encapsulate a cell on chess board.

class ChessBoard: def init(self, size=CHESS_BOARD_SIZE): self._size = size self._pieces = [] self._white_king_position = None self._black_king_position = None self._initialize_pieces(INITIAL_PIECE_SET_SINGLE)

## :encapsulate common functionality of all chess pieces.

class Piece(ABC): BLACK = "black" WHITE = "white"
class PieceFactory: @staticmethod def create(piece_type: str, position: ChessPosition, color): 
if piece_type == PieceType.KING: return King(position, color)

## :To encapsulate King as a chess piece.

rom .pieces import Piece from .moves import ChessPosition
class King(Piece): SPOT_INCREMENTS = [(1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)]

## :To encapsulate Queen as a chess piece.

from .pieces import Piece
class Queen(Piece): BEAM_INCREMENTS = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]

## :To encapsulate Knight as a chess piece.

from .pieces import Piece
 class Knight(Piece): SPOT_INCREMENTS = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

## :To encapsulate Rook as a chess piece.

from .pieces import Piece
class Rook(Piece): BEAM_INCREMENTS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

## :To encapsulate Bishop as a chess piece.

from .pieces import Piece
class Bishop(Piece): BEAM_INCREMENTS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

## :To encapsulate Pawn as a chess piece.

from .pieces import Piece from .moves import ChessPosition
class Pawn(Piece): SPOT_INCREMENTS_MOVE = [(0, 1)] SPOT_INCREMENTS_MOVE_FIRST = [(0, 1), (0, 2)] SPOT_INCREMENTS_TAKE = [(-1, 1), (1, 1)]

## :To encapsulate a chess move.

class ChessPosition: def init(self, x_coord, y_coord): self.x_coord = x_coord self.y_coord = y_coord
class MoveCommand: def init(self, src: ChessPosition, dst: ChessPosition): self.src = src self.dst = dst

## :To encapsulate a chess game.

class ChessGameState: def init(self, pieces, board_size): self.pieces = pieces self.board_size = board_size
class ChessGame: STATUS_WHITE_MOVE = "white_move" STATUS_BLACK_MOVE = "black_move" STATUS_WHITE_VICTORY = "white_victory" STATUS_BLACK_VICTORY = "black_victory"

## :To encapsulate a chess render.

 from .moves import ChessPosition
 class InputRender: def render(self, game_state): raise NotImplementedError

class ConsoleRender(InputRender): def render(self, game): for i in reversed(range(0, game.board_size)): self._draw_board_line(i, game.pieces, game.board_size) self._draw_bottom_line(game.board_size)

## :To encapsulate a chess player.

 from .render import ConsoleRender from .game import ChessGame
 class Player: def play_chess(self): render = ConsoleRender() game = ChessGame(render) game.run()
 if name == "main": player = Player player.play_chess()
