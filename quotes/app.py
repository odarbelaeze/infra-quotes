import os
import random

import falcon

from quotes.content import DEFAULT_QUOTES


class Storage(object):

    def __init__(self, quotes=None):
        self.quotes = quotes if quotes else DEFAULT_QUOTES

    def random(self):
        return random.choice(self.quotes)


class RandomQuoteResource(object):

    def __init__(self):
        self.storage = Storage()

    def on_get(self, req, res):
        res.media = {
            'data': self.storage.random(),
        }


def create_app():
    app = falcon.API()
    prefix = os.environ.get('QUOTES_PREFIX', '')
    app.add_route(f'{prefix}/quote/random', RandomQuoteResource())
    return app


APP = create_app()
