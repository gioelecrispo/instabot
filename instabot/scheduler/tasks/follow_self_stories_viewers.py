from instabot.list_utils import diff
from .. import Task


class FollowSelfStoriesViewersNotFollowing(Task):
    task_id = "follow_self_stories_viewers_not_following"
    task_name = "Follow self stories viewers not following"
    default_config = {}
    default_schedule = {"value": 1, "time_unit": "days"}

    def do(self):
        """Follows the viewers of my stories that are not following me """
        story_viewers_dict = self.bot.get_self_stories_viewers()
        my_followers = self.bot.followers
        viewers = []
        for story_id, story_dict in story_viewers_dict.items():
            for user in story_dict["users"]:
                viewers.append(str(user["pk"]))
        to_follow = diff(viewers, my_followers)
        for user in to_follow:
            self.bot.follow(user)
