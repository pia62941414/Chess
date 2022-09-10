    if piece_type == PieceType.QUEEN:
        return Queen(position, color)
    
    if piece_type == PieceType.KNIGHT:
        return Knight(position, color)
    
    if piece_type == PieceType.ROOK:
        return Rook(position, color)
    
    if piece_type == PieceType.BISHOP:
        return Bishop(position, color)
    
    if piece_type == PieceType.PAWN:
        return Pawn(position, color)