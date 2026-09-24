#!/usr/bin/env python3

from checkmate import checkmate

def main():
    board = None
    error = checkmate(board)
    if error:
        print("Error:", error)

if __name__ == "__main__":
    main()