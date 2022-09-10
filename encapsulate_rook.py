def get_threatened_positions(self, board):
    positions = []
    for increment in Rook.BEAM_INCREMENTS:
        positions += board.beam_search_threat(self._position, self._color, increment[0], increment[1])
    return positions

def get_moveable_positions(self, board):
    return self.get_threatened_positions(board)

def _symbol_impl(self):
    return 'RO'