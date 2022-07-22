from telebot import handle, events, send, filters, ctx
from assets import scenes, config, sessions


@handle(events.start)
def _():
    send('Hello')



