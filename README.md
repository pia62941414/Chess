# Chess

To encapsulate a chess player

from .render import ConsoleRender from .game import ChessGame
class Player: def play_chess(self): render = ConsoleRender() game = ChessGame(render) game.run()
if name == "main": player = Player player.play_chess()
