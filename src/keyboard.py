from src.item import Item


class Language:
    LANG = {True: 'EN', False: 'RU'}

    def __init__(self):
        self._language = True

    @property
    def language(self):
        return self.LANG[self._language]

    def change_lang(self):
        self._language = not self._language
        return self

    def __str__(self):
        return self.LANG[self._language]


class Keyboard(Item, Language):
    pass
