from telebot import Session


class NewPost(Session):
    photos: list
    channel: str
    sign: str
