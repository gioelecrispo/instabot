from instabot.scheduler import BotScheduler

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from .test_bot import TestBot


#class TestBotScheduler:


    #def setup(self):
    #    self.USERNAME = "test_username"
    #    self.PASSWORD = "test_password"
    #    self.task_ids = ["stats"]
    #    self.scheduler = self.__create_scheduler__(self.USERNAME, self.PASSWORD)

    #@patch('instabot.Bot.__init__')
    #def __create_scheduler__(self, username, password):
        #return BotScheduler(username, password)
