from tasks.task_01 import find_occurrences
import pytest

test_tree = {"first": ["RED", "BLUE"],
             "second": {
                 "simple_key": ["GREEN", "list", "of", "RED", "valued"],
             },
             "third": {
                 "abc": "BLUE",
                 "jhl": "RED",
                 "complex_key": {
                     "key1": "value1",
                     "key2": "RED",
                     "key3": ["a", "lot", "GREEN", "GREEN",
                              {"nested_key": "RED"}],
                 }
             },
             "fourth": "RED",
             }


@pytest.mark.parametrize('tree, elem, expected_res', [(test_tree, 'RED', 6),
                                                      (test_tree, 'BLUE', 2),
                                                      (test_tree, 'GREEN', 3)])
def test_find_positive(tree, elem, expected_res):
    assert expected_res == find_occurrences(tree, elem)


@pytest.mark.parametrize('tree, elem, expected_res', [(test_tree, 'RED', 13),
                                                      (test_tree, 'BLUE', 4),
                                                      (test_tree, 'GREEN', 8)])
def test_find_negative(tree, elem, expected_res):
    assert not expected_res == find_occurrences(tree, elem)


@pytest.mark.parametrize('tree, elem, expected_exception', [(test_tree, None, ValueError),
                                                            (test_tree, None, ValueError),
                                                            (test_tree, None, ValueError)])
def test_find_exceptions(tree, elem, expected_exception):
    with pytest.raises(expected_exception):
        find_occurrences(tree, elem)
