from instabot.scheduler.tasks import Stats
from instabot.scheduler.tasks import FollowSelfStoriesViewersNotFollowing
from instabot.scheduler.tasks import \
    UnfollowFollowersWithHighFollowingFollowerRatio
from tests.test_bot import TestBot

try:
    from unittest.mock import Mock, patch
except ImportError:
    from mock import Mock, patch


class TestStats(TestBot):

    def test_stats(self):
        task = Stats(self.bot)
        task.execute()


class TestFollowSelfStoriesViewersNotFollowing(TestBot):

    def test_stats(self):
        task = FollowSelfStoriesViewersNotFollowing(self.bot)
        task.execute()


class TestUnfollowFollowersWithHighFollowingFollowerRatio(TestBot):

    def test_stats(self):
        task = UnfollowFollowersWithHighFollowingFollowerRatio(self.bot)
        task.execute()