"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(inp_cls):
    def __init__(self):
        inp_cls.total_objects += 1

    @classmethod
    def get_created_instances(cls):
        return cls.total_objects

    @classmethod
    def reset_instances_counter(cls):
        instances_value = cls.total_objects
        cls.total_objects = 0
        return instances_value

    setattr(inp_cls, 'total_objects', 0)
    setattr(inp_cls, '__init__', __init__)
    setattr(inp_cls, 'get_created_instances', get_created_instances)
    setattr(inp_cls, 'reset_instances_counter', reset_instances_counter)

    return inp_cls


@instances_counter
class User:
    pass


if __name__ == '__main__':
    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    print(user.get_created_instances())  # 3
    print(user.reset_instances_counter())  # 3
