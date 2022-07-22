from .base import Event

start = Event()


class Text(Event):

    def __init__(self, value: str = None):
        self.value = value

    def __call__(self, value: str):
        return Text(value)


text = Text()

photo = Event()
