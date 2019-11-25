import copy

import logging
import schedule
import time

import instabot.scheduler
from instabot import Bot


class BotScheduler:

    TASKS_DIRECTORY = "scheduler/tasks"

    def __init__(self, username, password):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        self.bots = dict()
        self.__create_bot__()
        # The login is done only once at startup to avoid multiple login.
        self.__login__(username, password)

    def __create_bot__(self):
        self.bots["original"] = Bot()
        self.logger.info("BOT-SCHEDULER - Bot <original> created")

    def __login__(self, username, password):
        self.bots["original"].login(username=username, password=password,
                                    force=False, use_cookie=True)
        self.logger.info("BOT-SCHEDULER - Login executed for Bot <original>")

    # def run(self, task_ids=None, task_configs=None, task_schedules=None):
    #     if task_ids is None:
    #         tasks_ids = import_tasks(self.TASKS_DIRECTORY)
    #     for task_name, task in self.configuration.
        #     task_params["schedule_config"].items():
    #         if task["active"]:
    #             self.bots[task_name] = copy.deepcopy(self.bots["original"])
    #             self.logger.info("BOT-SCHEDULER - Enabling schedule:
        #             <{}> every: {} {}".format(task["function_name"],
        #             task["schedule"]["value"], task["schedule"]
        #             ["time_unit"]))
    #             bot_function = getattr(bot_functions, task["function_name"])
    #             scheduler = schedule.every(task["schedule"]["value"])
    #             setattr(scheduler, "unit", task["schedule"]["time_unit"])
    #             # Schedule a task with the following inputs:
    #             #  - task_name,
    #             #  - bot related to that task,
    #             #  - configuration related to that task (scope limiting)
    #             scheduler.do(bot_function, task_name, self.bots[task_name],
    #                          self.configuration.task_params["task_config"]
        #                          [task_name])

        while True:
            schedule.run_pending()
            time.sleep(1)

    def execute(self, task_id, task_config):
        """ Run a single task, referencing it by task_id.
        You need only to specify task ids and configs you want to execute.
        This function creates a new Bot (through a deepcopy logic) and uses its
        logically separate environment to execute it.
        """
        self.bots[task_id] = copy.deepcopy(self.bots["original"])
        tasks = instabot.scheduler.import_tasks(self.TASKS_DIRECTORY)
        try:
            task = tasks[task_id]
            task(self.bots[task_id], task_config).execute()
        except KeyError:
            self.logger.error("BOT-SCHEDULER - No task with id {} found. "
                              "Abort.".format(task_id))

    def execute_multiple(self, task_ids, task_configs):
        """ Run multiple tasks, by using the execute function multiple times.
        You need only to specify task ids and configs you want to execute. """
        for task_id, task_config in zip(task_ids, task_configs):
            self.execute(task_id, task_config)
