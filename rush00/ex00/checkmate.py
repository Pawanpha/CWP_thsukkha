def checkmate(board):
    rows = board.splitlines()

    # Validate square board
    n = len(rows)
    if n == 0 or any(len(row) != n for row in rows):
        return "Invalid board"

    # Find the King
    king_pos = None
    for r in range(n):
        for c in range(n):
            if rows[r][c] == 'K':
                if king_pos is not None:
                    return "Only one king na ja"
                king_pos = (r, c)

    if king_pos is None:
        return "I need king"

    kr, kc = king_pos

    def first_piece_in_direction(dr, dc):
        r, c = kr + dr, kc + dc
        while 0 <= r < n and 0 <= c < n:
            ch = rows[r][c]
            print(ch)
            if ch in "PRBQK":
                return ch
            r += dr
            c += dc
        return None

    in_check = False

    # Rook / Queen attacks
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        piece = first_piece_in_direction(dr, dc)
        if piece in ("R", "Q"):
            in_check = True
            break

    # Bishop / Queen attacks
    if not in_check:
        for dr, dc in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            piece = first_piece_in_direction(dr, dc)
            if piece in ("B", "Q"):
                in_check = True
                break

    # Pawn attacks
    if not in_check:
        # Pawns attack diagonally upward (toward decreasing row index)
        for pr, pc in ((kr + 1, kc - 1), (kr + 1, kc + 1)):
            if 0 <= pr < n and 0 <= pc < n and rows[pr][pc] == 'P':
                in_check = True
                break

    print("Success" if in_check else "Fail")