from tasks import hw3
import pytest


@pytest.mark.parametrize('inp_sequence, expected_result', [([[1, 2], [3, 4]], [[1, 3], [1, 4], [2, 3], [2, 4]]),
                                                           ([[1, 2, 3], [4, 5, 6]],
                                                            [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4],
                                                             [3, 5], [3, 6]]),
                                                           ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                                                            [[1, 5, 9], [1, 5, 10], [1, 5, 11], [1, 5, 12], [1, 6, 9],
                                                             [1, 6, 10], [1, 6, 11], [1, 6, 12], [1, 7, 9], [1, 7, 10],
                                                             [1, 7, 11], [1, 7, 12], [1, 8, 9], [1, 8, 10], [1, 8, 11],
                                                             [1, 8, 12], [2, 5, 9], [2, 5, 10], [2, 5, 11], [2, 5, 12],
                                                             [2, 6, 9], [2, 6, 10], [2, 6, 11], [2, 6, 12], [2, 7, 9],
                                                             [2, 7, 10], [2, 7, 11], [2, 7, 12], [2, 8, 9], [2, 8, 10],
                                                             [2, 8, 11], [2, 8, 12], [3, 5, 9], [3, 5, 10], [3, 5, 11],
                                                             [3, 5, 12], [3, 6, 9], [3, 6, 10], [3, 6, 11], [3, 6, 12],
                                                             [3, 7, 9], [3, 7, 10], [3, 7, 11], [3, 7, 12], [3, 8, 9],
                                                             [3, 8, 10], [3, 8, 11], [3, 8, 12], [4, 5, 9], [4, 5, 10],
                                                             [4, 5, 11], [4, 5, 12], [4, 6, 9], [4, 6, 10], [4, 6, 11],
                                                             [4, 6, 12], [4, 7, 9], [4, 7, 10], [4, 7, 11], [4, 7, 12],
                                                             [4, 8, 9], [4, 8, 10], [4, 8, 11], [4, 8, 12]])])
def test_combinations_positive(inp_sequence, expected_result):
    assert hw3.combinations(*inp_sequence) == expected_result


@pytest.mark.parametrize('inp_value, expected_exception', [(123, TypeError),
                                                           (None, TypeError),
                                                           (341, TypeError),
                                                           ])
def test_combinations_exceptions(inp_value, expected_exception):
    with pytest.raises(expected_exception):
        hw3.combinations(inp_value)
