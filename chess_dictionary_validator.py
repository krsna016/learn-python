def valid_chess_validator(place,piece):
    """
    This function will check whether the chess board is arranged 
    correctly or not.
    """
    chess_board = {}
    white_pieces = chess_board.update({"1a":"W_ROOK","1b":"W_KNIGHT","1c":"W_BISHOP","1d":"W_QUEEN","1e":"W_KING","1f":"W_BISHOP","1g":"W_KNIGHT","1h":"W_ROOK"})
    white_pawns = dict.fromkeys(("2a","2b","2c","2d","2e","2f","2g","2h"),"W_PAWN")
    chess_board.update(white_pawns)
    black_pawns = dict.fromkeys(("7a","7b","7c","7d","7e","7f","7g","7h"),"B_PAWN")
    chess_board.update(black_pawns)
    black_pieces = chess_board.update({"8a":"B_ROOK","8b":"B_KNIGHT","8c":"B_BISHOP","8d":"B_QUEEN","8e":"B_KING","8f":"B_BISHOP","8g":"B_KNIGHT","8h":"B_ROOK"})
    if(chess_board[place] == piece):
        print("All correct !! The piece is in it's correct position.")
    else:
        place_is_this = tuple(i for i in chess_board if chess_board[i] == piece)
        print("Kindly place the'"+piece+"' to the position :",place_is_this)
        
valid_chess_validator("1a","B_BISHOP")