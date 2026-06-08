class Mock(object):
    def __init__(self, *args, **kwargs):
        self.call_args_list = []

    def __call__(self, *args, **kwargs):
        self.call_args_list.append((args, kwargs))
