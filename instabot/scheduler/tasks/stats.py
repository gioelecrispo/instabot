from .. import Task


class Stats(Task):
    task_id = "stats"
    task_name = "Compute statistics"
    default_config = {}
    default_schedule = {"value": 1, "time_unit": "hours"}

    def do(self):
        self.bot.save_user_stats(self.bot.user_id)
