from . import events
from .filters import filters


class Session:
    pass


class Context:
    pass


ctx = Context()


def run(): ...


def send(*args): ...


class Scene:
    ...


def handle(event, scene=None):
    def deco(callback):
        return callback

    return deco
