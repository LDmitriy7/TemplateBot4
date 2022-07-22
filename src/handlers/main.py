from telebot import handle, events, send, ctx, enter
from assets import sessions, scenes


@handle(events.start)
def _():
    send('Отправь мне картинки')


@handle(events.photo)
def _(s: sessions.NewPost):
    s.photos.append(ctx.photo_id)
    send('В какой канал отправить?')
    enter(scenes.new_post)
