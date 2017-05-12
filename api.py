import config
from bot import Bot
from flask import Flask
from flask_restful import Resource, Api

bot = Bot(config.FACEBOOK_EMAIL, config.FACEBOOK_PASSWORD)

app = Flask(__name__)
api = Api(app)
tinder_api = bot.session._api

class Matches(Resource):
    def get(self):
        return tinder_api.matches(None)

class Match(Resource):
    def get(self, match_id):
        match = {}
        for m in tinder_api.matches(None):
            if m['_id'] == match_id:
                match = m
                break
        return match

api.add_resource(Matches, '/matches/')
api.add_resource(Match, '/matches/<match_id>/')

if __name__ == '__main__':
    app.run(debug=True)