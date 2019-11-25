from instabot.list_utils import commons
from instabot.random_utils import choose_random
from .. import Task


class UnfollowFollowersWithHighFollowingFollowerRatio(Task):
    task_id = "unfollow_followers_with_high_following_follower_ratio"
    task_name = "Unfollow followers with high following / follower Ratio"
    default_config = {
        "number_of_users_to_unfollow": 5,
        "ratio": 3
    }
    default_schedule = {"value": 3, "time_unit": "hours"}

    def do(self):
        num_of_user_to_unfollow = self.config["number_of_users_to_unfollow"]
        # We take only people that follow us and followed by us
        followers_following = commons(self.bot.followers, self.bot.following)
        if len(followers_following) < num_of_user_to_unfollow:
            num_of_user_to_unfollow = len(followers_following)
        followers_to_unfollow = choose_random(followers_following,
                                              k=num_of_user_to_unfollow)
        for user_id in followers_to_unfollow:
            user_info = self.bot.get_user_info(user_id)
            follower_count = user_info["follower_count"]
            following_count = user_info["following_count"]
            if follower_count != 0:
                ratio = float(following_count / follower_count)
                if ratio > self.config["ratio"]:
                    self.bot.unfollow(user_id)


