from typing import List

from tasks.task_03 import tic_tac_toe_checker
import pytest


@pytest.mark.parametrize('board, expected', [([['o', 'x', 'o'],
                                               ['x', 'o', 'o'],
                                               ['o', 'o', 'x']], 'o wins!'),
                                             ([['o', 'x', 'o'],
                                               ['x', 'x', 'o'],
                                               ['o', 'x', 'x']], 'x wins!'),
                                             ([['o', 'x', 'o'],
                                               ['x', '-', 'o'],
                                               ['o', 'o', 'x']], 'unfinished!'),
                                             ([['o', 'x', 'o'],
                                               ['x', 'x', 'o'],
                                               ['o', 'o', 'x']], 'draw!')
                                             ])
def test_checker_positive(board: List[List], expected: str):
    assert tic_tac_toe_checker(board) == expected


@pytest.mark.parametrize('board, expected', [([['o', 'x', 'o'],
                                               ['x', 'o', 'o'],
                                               ['o', 'o', 'x']], 'x wins!'),
                                             ([['o', 'x', 'o'],
                                               ['x', 'x', 'o'],
                                               ['o', 'x', 'x']], 'o wins!'),
                                             ([['o', 'x', 'o'],
                                               ['x', '-', 'o'],
                                               ['o', 'o', 'x']], 'draw!'),
                                             ([['o', 'x', 'o'],
                                               ['x', 'x', 'o'],
                                               ['o', 'o', 'x']], 'unfinished!')
                                             ])
def test_checker_positive(board: List[List], expected: str):
    assert not tic_tac_toe_checker(board) == expected


@pytest.mark.parametrize('board, expected', [('', TypeError),
                                             (None, TypeError),
                                             ('', TypeError)])
def test_checker_positive(board: List[List], expected: Exception):
    with pytest.raises(expected):
        tic_tac_toe_checker(board)
