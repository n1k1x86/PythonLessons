class Filter:
    """
        Helper filter class. Accepts a list of single-argument
        functions that return True if object in list conforms to some criteria
    """

    def __init__(self, *functions):
        self.functions = functions

    def apply(self, data):
        return [
            item for item in data
            if all(i(item) for i in self.functions)
        ]


def make_filter(**keywords):
    """
        Generate filter object for specified keywords
    """
    filter_funcs = []

    def keyword_filter_func(input_data):
        for key, value in keywords.items():
            if (key, value) in input_data.items():
                return True
        return False

    filter_funcs.append(keyword_filter_func)
    return Filter(*filter_funcs)


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
