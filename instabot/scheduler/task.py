from abc import ABCMeta, abstractmethod

from .task_decorators import BotTask
from .task_decorators import ExceptionHandler
from .task_decorators import ThreadedTask


class Task:
    __metaclass__ = ABCMeta

    task_id = "task_id"
    task_name = "task_name"
    default_config = {}
    default_schedule = {"value": 3, "time_unit": "hours"}

    def __init__(self, bot, config=None, schedule=None):
        self.bot = bot
        if config is None:
            self.config = self.default_config
        else:
            self.config = config
        if config is None:
            self.schedule = self.default_schedule
        else:
            self.schedule = schedule

    @BotTask
    @ThreadedTask
    @ExceptionHandler
    def execute(self):
        self.do()

    @abstractmethod
    def do(self):
        pass

    def __repr__(self):
        return "task_id: " + self.task_id + "; task_name: " + self.task_name
