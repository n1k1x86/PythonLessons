import pytest
from tasks.oop_1_classes.homework import Homework, WrongDeadlineDaysException, WrongTextException


@pytest.mark.parametrize('positive_object', [Homework("Test task", 3),
                                             Homework("The second test task", 10),
                                             Homework("The third test task", 1)])
def test_is_active_positive(positive_object):
    assert positive_object.is_active()


@pytest.mark.parametrize('negative_object', [Homework("False test task", 0),
                                             Homework("The second test task", 0),
                                             Homework("The third test task", 0)])
def test_is_active_negative(negative_object):
    assert not negative_object.is_active()


@pytest.mark.parametrize('input_data, expected_exception', [(["False test task", None], WrongDeadlineDaysException),
                                                            (["False test task", -10], WrongDeadlineDaysException),
                                                            (["False test task", '10'], WrongDeadlineDaysException),
                                                            ([None, 0], WrongTextException),
                                                            ([10, 2], WrongTextException),
                                                            ([30, None], WrongTextException),
                                                            ([99999, None], WrongTextException)])
def test_init_exceptions(input_data, expected_exception):
    with pytest.raises(expected_exception):
        Homework(*input_data)
