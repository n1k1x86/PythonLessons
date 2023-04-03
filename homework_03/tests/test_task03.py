from tasks import task03
import pytest


def test_filter_part_one_positive():
    expected_res = [x for x in range(0, 100) if x % 2 == 0 and x != 0]
    positive_evens = task03.Filter(lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int))
    assert positive_evens.apply(range(100)) == expected_res


def test_filter_part_one_exceptions():
    positive_evens = task03.Filter(lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(int, a))
    with pytest.raises(TypeError):
        positive_evens.apply(range(100))


def test_filter_part_two_positive():
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {
            "is_dead": True,
            "kind": "parrot",
            "type": "bird",
            "name": "polly"
        }
    ]
    expected_result = task03.make_filter(name='polly', type='bird').apply(sample_data)
    assert expected_result == [sample_data[1]]
