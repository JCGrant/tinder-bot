import pynder
from token_util import get_token


class Bot:
    def __init__(self, fb_id, fb_email, fb_password):
        self.fb_id = fb_id
        self.fb_email = fb_email
        self.fb_password = fb_password
        self.renew_session()
    
    def renew_session(self):
        print("Obtaining new token")
        new_token = get_token(self.fb_email, self.fb_password)
        print("Creating new pynder Session")
        self.session = pynder.Session(facebook_id=self.fb_id, facebook_token=new_token)