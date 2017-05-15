import config
from bot import Bot
from flask import Flask
from flask_restful import Resource, Api
from flask_socketio import SocketIO

bot = Bot(config.FACEBOOK_EMAIL, config.FACEBOOK_PASSWORD)

app = Flask(__name__)
api = Api(app)
socket = SocketIO(app)

def get_updates():
    return bot.session._api.updates(None)

class Matches(Resource):
    def get(self):
        return get_updates().get('matches')

class Match(Resource):
    def get(self, match_id):
        match = {}
        for m in get_updates().get('matches'):
            if m['_id'] == match_id:
                match = m
                break
        return match

api.add_resource(Matches, '/matches/')
api.add_resource(Match, '/matches/<match_id>/')

if __name__ == '__main__':
    socket.run(app, debug=True)