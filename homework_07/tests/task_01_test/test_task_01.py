import pytest
from tasks.task_01 import merge_sorted_files


def create_test_data(test_data):
    test_files = ['testfile01.txt', 'testfile02.txt', 'testfile03.txt']
    for ind, file in enumerate(test_files):
        with open(file, 'w') as f:
            for data in test_data[ind]:
                for num in data:
                    f.write(num + '\n')


@pytest.mark.parametrize('test_data, expected', [
    ([['1', '3', '5'], ['2', '4', '6'], ['7', '8', '9']], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([['1', '3'], ['2', '6'], ['7', '8', '9']], [1, 2, 3, 6, 7, 8, 9]),
    ([['1'], ['2', '4'], ['7', '8']], [1, 2, 4, 7, 8]),
    ([['3', '5'], ['2', '6'], ['9']], [2, 3, 5, 6, 9])])
def test_merge_sort_positive(test_data, expected):
    create_test_data(test_data)
    files = ['testfile01.txt', 'testfile02.txt', 'testfile03.txt']
    assert list(merge_sorted_files(files)) == expected


@pytest.mark.parametrize('test_data, non_expected', [
    ([['1', '3', '5'], ['2', '4', '6'], ['7', '8', '9']], [1, 2, 3, 4, 5, 9]),
    ([['1', '3'], ['2', '6'], ['7', '8', '9']], [1, 2, 3, 6, 8, 9]),
    ([['1'], ['2', '4'], ['7', '8']], [1, 2, 4]),
    ([['3', '5'], ['2', '6'], ['9']], [2, 3, 6, 9])])
def test_merge_sort_negative(test_data, non_expected):
    create_test_data(test_data)
    files = ['testfile01.txt', 'testfile02.txt', 'testfile03.txt']
    assert not list(merge_sorted_files(files)) == non_expected


@pytest.mark.parametrize('input_data, exp_exception', [(123, TypeError),
                                                       (1233, TypeError),
                                                       (134134, TypeError),
                                                       (None, TypeError)])
def test_merge_sort_exceptions(input_data, exp_exception):
    with pytest.raises(exp_exception):
        merge_sorted_files(input_data)
