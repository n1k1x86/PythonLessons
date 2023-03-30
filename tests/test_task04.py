from tasks import task04
import pytest
from typing import List


@pytest.mark.parametrize('list_a, list_b, list_c, list_d, expected_res', [([-9, -97, 15, -23, -100, 95, -25, 41, -68,
                                                                            22, -60, -64, -86, -45, 30, -52, -76, 2,
                                                                            73, 9],
                                                                           [64, 62, 75, -25, 30, 3, -12, -60, 78, -90,
                                                                            80, 70, -55, -38, 36, -37, -62, 94, -21,
                                                                            68],
                                                                           [-27, 10, -98, 54, -57, -69, 67, -2, -15,
                                                                            12, -26, -63, -23, -26, -85, 45, 19, 57,
                                                                            61, -90],
                                                                           [83, -11, -53, 53, -14, -45, -83, 47, 95,
                                                                            63, -42, -65, -73, -81, 71, -81, -8, -81,
                                                                            66, 80], 525),
                                                                          ([-55, 66, -78, -90, -26, -27, -39, -63, 16,
                                                                            -46, 91, 65, 91, 59, -99, -90, -86, -18,
                                                                            -81, 21],
                                                                           [77, 30, 77, 29, -69, -97, 65, 66, -91, 34,
                                                                            -91, -26, -59, -80, 26, 43, -25, 49, 61,
                                                                            20],
                                                                           [-51, -36, 57, 40, 23, -75, -18, -82, 99,
                                                                            -25, -71, -64, 70, 33, 31, -63, -96, -54,
                                                                            -40, -25],
                                                                           [-62, -83, -86, 78, 54, 52, 63, -8, 0, 5, 48,
                                                                            -98, 89, -94, 24, -67, -99, 0, -58, -3],
                                                                           449)])
def test_check_sum_of_four_positive(list_a: List, list_b: List, list_c: List, list_d: List, expected_res: int):
    assert task04.check_sum_of_four(list_a, list_b, list_c, list_d) == expected_res


@pytest.mark.parametrize('list_a, list_b, list_c, list_d, non_expected_res',
                         [([-9, -97, 15, -23, -100, 95, -25, 41, -68,
                            22, -60, -64, -86, -45, 30, -52, -76, 2,
                            73, 9],
                           [64, 62, 75, -25, 30, 3, -12, -60, 78, -90,
                            80, 70, -55, -38, 36, -37, -62, 94, -21,
                            68],
                           [-27, 10, -98, 54, -57, -69, 67, -2, -15,
                            12, -26, -63, -23, -26, -85, 45, 19, 57,
                            61, -90],
                           [83, -11, -53, 53, -14, -45, -83, 47, 95,
                            63, -42, -65, -73, -81, 71, -81, -8, -81,
                            66, 80], 505),
                          ([-55, 66, -78, -90, -26, -27, -39, -63, 16,
                            -46, 91, 65, 91, 59, -99, -90, -86, -18,
                            -81, 21],
                           [77, 30, 77, 29, -69, -97, 65, 66, -91, 34,
                            -91, -26, -59, -80, 26, 43, -25, 49, 61,
                            20],
                           [-51, -36, 57, 40, 23, -75, -18, -82, 99,
                            -25, -71, -64, 70, 33, 31, -63, -96, -54,
                            -40, -25],
                           [-62, -83, -86, 78, 54, 52, 63, -8, 0, 5, 48,
                            -98, 89, -94, 24, -67, -99, 0, -58, -3],
                           49)])
def test_check_sum_of_four_negative(list_a: List, list_b: List, list_c: List, list_d: List, non_expected_res: int):
    assert task04.check_sum_of_four(list_a, list_b, list_c, list_d) != non_expected_res


@pytest.mark.parametrize('inp01, inp02, inp03, inp04, expected_exception', [(12, 12, 12, 12, TypeError),
                                                                            (12, -2, 12, 'sdsd', TypeError),
                                                                            ([123], 134, "ewqeqe", -500, TypeError)])
def test_check_sum_of_four_exceptions(inp01, inp02, inp03, inp04, expected_exception):
    with pytest.raises(expected_exception):
        task04.check_sum_of_four(inp01, inp02, inp03, inp04)
