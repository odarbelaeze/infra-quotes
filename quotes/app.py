import falcon
import random

from quotes.content import DEFAULT_QUOTES

class Storage(object):

    def __init__(self, quotes=None):
        self.quotes = quotes if quotes else DEFAULT_QUOTES

    def random(self):
        return random.choice(self.quotes)


class QuotesResource(object):

    def __init__(self):
        self.storage = Storage()

    def on_get(self, req, res):
        res.media = {
            'data': self.storage.random(),
        }


def create_app():
    app = falcon.API()
    app.add_route('/quotes', QuotesResource())
    return app


APP = create_app()
