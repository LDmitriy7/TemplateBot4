from telebot import handle, events, send


@handle(events.start)
def _():
    send('Отправь мне картинки')


@handle(events.photo)
def _():
    send('?')
