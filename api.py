import config
from bot import Bot
from flask import Flask
from flask_restful import Resource, Api

bot = Bot(config.FACEBOOK_EMAIL, config.FACEBOOK_PASSWORD)

app = Flask(__name__)
api = Api(app)

def get_matches():
    if bot.running:
        return bot.matches_json
    else:
        return bot.session._api.matches(None)

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
    bot.start()
    app.run(debug=True)