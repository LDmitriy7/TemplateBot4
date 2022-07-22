class Filters:
    def __call__(self, **kwargs):
        def deco(handler):
            return handler

        return deco


filters = Filters()
