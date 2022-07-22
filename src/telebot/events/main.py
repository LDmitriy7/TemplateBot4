class Event:
    pass


start = Event()


class TextEvent(Event):

    def __init__(self, value: str = None):
        self.value = value

    def __call__(self, value: str):
        return TextEvent(value)


text = TextEvent()
