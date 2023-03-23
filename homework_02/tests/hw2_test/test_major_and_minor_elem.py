from tasks import hw2
import pytest


@pytest.mark.parametrize('inp_sequence, expected_result', [([3, 2, 3], (3, 2)),
                                                           ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
                                                           ([2, 1, 1, 1, 1, 2, 2], (1, 2)),
                                                           ([5, 5, 6, 6, 6, 6, 5], (6, 5)),
                                                           ([0, 0, 1, 0, 0, 0, 0], (0, 1)),
                                                           ([20, 20, 10, 10, 10, 20, 20], (20, 10)),
                                                           ([2, 2, 7, 7, 7, 2, 7], (7, 2)),
                                                           ([2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2,
                                                             2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1,
                                                             2, 2], (2, 1))])
def test_major_and_minor_elem_positive(inp_sequence, expected_result):
    assert hw2.major_and_minor_elem(inp_sequence) == expected_result


@pytest.mark.parametrize('inp_sequence, wrong_result', [([3, 2, 3], (2, 3)),
                                                           ([2, 2, 1, 1, 1, 2, 2], (1, 2)),
                                                           ([2, 1, 1, 1, 1, 2, 2], (2, 1)),
                                                           ([5, 5, 6, 6, 6, 6, 5], (5, 6)),
                                                           ([0, 0, 1, 0, 0, 0, 0], (1, 0)),
                                                           ([20, 20, 10, 10, 10, 20, 20], (10, 20)),
                                                           ([2, 2, 7, 7, 7, 2, 7], (2, 7)),
                                                           ([2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2,
                                                             2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1,
                                                             2, 2], (1, 2))])
def test_major_and_minor_elem_negative(inp_sequence, wrong_result):
    assert hw2.major_and_minor_elem(inp_sequence) != wrong_result


@pytest.mark.parametrize('inp_seq, expected_exception', [(123, TypeError),
                                                         (12, TypeError),
                                                         (5443, TypeError),
                                                         (34345, TypeError),
                                                         (65424, TypeError)])
def test_major_and_minor_elem_exceptions(inp_seq, expected_exception):
    with pytest.raises(expected_exception):
        hw2.major_and_minor_elem(inp_seq)
