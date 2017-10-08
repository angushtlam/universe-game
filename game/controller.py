import time

from util import wikipedia as util_wikipedia


def current_milli_time():
    return int(round(time.time() * 1000))


class Game():
    def __init__(self):
        self.game_in_progress = False
        self.start_timestamp = 0
        self.start_page = None
        self.end_page = None
        self.players = {}

    def start_new_game(self):
        self.game_in_progress = True
        self.start_timestamp = current_milli_time()
        self.start_page = util_wikipedia.get_url_by_article_id(
                                util_wikipedia.get_random_article_id()
                            )
        self.end_page = util_wikipedia.get_url_by_article_id(
                                util_wikipedia.get_random_article_id()
                            )
        self.players = {}
        return True

    def get_game_status(self):
        return {
            'start_timestamp': self.start_timestamp,
            'start_page': self.start_page,
            'end_page': self.end_page,
            'players': self.players
        }

    def update_player(self, name, page):
        if self.players.get(name, None) is None:
            self.players[name] = []

        self.players[name].append(page)
        return True
