from . import events
from .events.base import Event
from .filters import filters
from . import core


class Session:
    pass


class Context:
    pass


ctx = Context()


def run():
    core.run()


def send(text: str):
    core.bot.send_message(text)


class Scene:
    ...


def handle(event: Event, scene: str = None):
    if event == events.start:
        handler = core.on.command('start', state=scene)
    elif event == events.photo:
        handler = core.on.photo(state=scene)
    else:
        raise ValueError('Invalid event')

    def deco(callback):
        handler(callback)
        return callback

    return deco
