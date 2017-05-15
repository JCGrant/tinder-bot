import config
from bot import Bot
from flask import Flask
from flask_restful import Resource, Api
from flask_socketio import SocketIO
from werkzeug.contrib.cache import SimpleCache

bot = Bot(config.FACEBOOK_EMAIL, config.FACEBOOK_PASSWORD)

app = Flask(__name__)
api = Api(app)
socket = SocketIO(app)

cache = SimpleCache()

def get_updates():
    if not cache.has('updates'):
        cache.set('updates', bot.session._api.updates(None), timeout=5 * 60)
    return cache.get('updates')

def get_matches():
    return get_updates().get('matches')

class Matches(Resource):
    def get(self):
        return get_matches()

class Match(Resource):
    def get(self, match_id):
        match = {}
        for m in get_matches():
            if m['_id'] == match_id:
                match = m
                break
        return match

api.add_resource(Matches, '/matches/')
api.add_resource(Match, '/matches/<match_id>/')

if __name__ == '__main__':
    socket.run(app, debug=True)