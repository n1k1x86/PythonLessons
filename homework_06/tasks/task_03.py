"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    count_empty = 0

    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return f"{board[0][0]} wins"
    if len(set([board[i][len(board) - i - 1] for i in range(len(board))])) == 1:
        return f"{board[0][len(board) - 1]} wins!"

    for comb in board:
        if len(set(comb)) == 1:
            return f"{list(set(comb))[0]} wins!"
        count_empty += comb.count('-')

    board_transp = list(map(lambda *row: list(row), *board))

    for comb in board_transp:
        if len(set(comb)) == 1:
            return f"{list(set(comb))[0]} wins!"
        count_empty += comb.count('-')

    if count_empty != 0:
        return 'unfinished!'

    return 'draw!'
