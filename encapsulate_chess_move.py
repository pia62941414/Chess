def __str__(self):
    return chr(ord("a") + self.x_coord) + str(self.y_coord + 1)

def __eq__(self, other):
    return self.x_coord == other.x_coord and self.y_coord == other.y_coord

@staticmethod
def from_string(string: str):
    return ChessPosition(ord(string[0]) - ord("a"), int(string[1:]) - 1)






@staticmethod
def from_string(string: str):
    tokens = string.split(" ")
    if len(tokens) != 2:
        return None
    src = ChessPosition.from_string(tokens[0])
    dst = ChessPosition.from_string(tokens[1])
    if src is None or dst is None:
        return None
    return MoveCommand(src, dst)