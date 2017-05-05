import os
import pynder
import config


class Bot:
    def __init__(self, fb_id=None, fb_token=None):
        self.session = pynder.Session(facebook_id=fb_id, facebook_token=fb_token)