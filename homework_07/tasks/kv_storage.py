class KeyValueStorage(object):
    """
    A wrapper class for this key value storage that works like this:

    storage = KeyValueStorage('path_to_file.txt')
    that has its keys and values accessible as collection items and as attributes.
    Example:
    storage['name']  # will be string 'kek'
    storage.song_name  # will be 'shadilay'
    storage.power  # will be integer 9001
    """
    my_dict = {}

    def __init__(self, path):
        self.path = path
        self.read_a_file()

    def read_a_file(self):
        with open(self.path) as f:
            while True:
                line = f.readline().split('=')
                if line == ['']:
                    break
                if not hasattr(self, line[0]):
                    setattr(self, line[0], line[1][0:len(line[1]) - 1])
                    self.my_dict[line[0]] = line[1][0:len(line[1]) - 1]

    def __getitem__(self, key):
        return self.my_dict[key]


kv = KeyValueStorage("storage.txt")
print(kv['name'])
print(kv.song)
print(kv.power)
