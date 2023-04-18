import pytest
from tasks.counter import instances_counter


@instances_counter
class TestClass1(object):
    pass


@instances_counter
class TestClass2(object):
    pass


@instances_counter
class TestClass3(object):
    pass


@pytest.mark.parametrize('parent_class, list_of_objects, expected', [(TestClass1, [TestClass1(), TestClass1()], 2),
                                                                     (TestClass2, [TestClass2()], 1),
                                                                     (TestClass3,
                                                                      [TestClass3(), TestClass3(), TestClass3()], 3)])
def test_counter_positive_get_count(parent_class, list_of_objects, expected):
    list_of_objects
    assert parent_class.get_created_instances() == expected


@pytest.mark.parametrize('parent_class', [TestClass1, TestClass2, TestClass3])
def test_counter_positive_reset(parent_class):
    parent_class.reset_instances_counter()
    assert parent_class.get_created_instances() == 0
