import pynder
from fb_auth_util import get_auth_details
from threading import Thread


class Bot:
    def __init__(self, fb_email, fb_password):
        self.fb_email = fb_email
        self.fb_password = fb_password
        self.renew_session()
    
    def renew_session(self):
        print("Obtaining Facebook ID and Token")
        fb_id, fb_token = get_auth_details(self.fb_email, self.fb_password)
        print("Creating new pynder Session")
        self.session = pynder.Session(facebook_id=fb_id, facebook_token=fb_token)

    def keep_fetching_matches(self):
        while True:
            self.matches = list(self.session.matches())

    def start(self):
        bot_thread = Thread(target=self.keep_fetching_matches, daemon=True)
        bot_thread.start()