"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
    },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    cnt = 0

    def get_elem(tree_elem: Any, elem: Any, count):
        for value in tree_elem.values() if isinstance(tree_elem, dict) else tree_elem:
            if value == elem:
                count = get_elem(value, elem, count) + 1
            elif isinstance(value, (list, tuple, set)):
                count = get_elem(value, elem, count)
            elif isinstance(value, dict):
                count = get_elem(value.values(), elem, count)
        return count

    return get_elem(tree, element, cnt)
