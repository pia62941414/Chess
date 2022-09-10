def get_threatened_positions(self, board):
    positions = []
    for increment in Knight.SPOT_INCREMENTS:
        positions.append(board.spot_search_threat(self._position, self._color, increment[0], increment[1]))
    positions = [x for x in positions if x is not None]
    return positions

def get_moveable_positions(self, board):
    return self.get_threatened_positions(board)

def _symbol_impl(self):
    return 'KN'