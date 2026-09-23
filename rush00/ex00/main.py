#!/usr/bin/env python3

from rush00.ex00.checkmate import checkmate

def main():
    board = """\
...Q.
.R...
..K..
...P.
.....\
"""
    error = checkmate(board)
    if error:
        print("Error:", error)

if __name__ == "__main__":
    main()