import time

import pytest

from instabot import Bot
from instabot.scheduler.exceptions import ActionBlockedException
from instabot.scheduler.task_decorators import BotTask
from instabot.scheduler.task_decorators import ExceptionHandler
from instabot.scheduler.task_decorators import ThreadedTask


class TestBotTask:

    def setup(self):
        self.task_id = "task_id"
        self.task_name = "task_name"
        self.bot = Bot()
        self.config = {}
        self.schedule = {}

    @BotTask
    def do(self):
        return "ok"

    def test_bot_task(self):
        result = self.do()
        assert result == "ok"


class TestThreadedRunTask:

    def setup(self):
        self.task_id = "task_id"
        self.task_name = "task_name"
        self.bot = Bot()
        self.config = {"run": True}
        self.schedule = {}

    @ThreadedTask
    def do(self):
        while self.config["run"]:
            time.sleep(0.5)

    def test_run_threaded(self):
        thread_control = self.do()
        self.config["run"] = False
        thread_control.join(1)
        assert thread_control is not None


class TestExceptionHandlerTask:

    def __init__(self):
        self.task_id = "task_id"
        self.task_name = "task_name"
        self.bot = Bot()
        self.config = {"throw_exception": False}
        self.schedule = {}

    @ExceptionHandler
    def do(self):
        if self.config["throw_exception"]:
            raise ActionBlockedException("Lanched Exception")
        else:
            return "ok"

    def test_exception_handler_no_ex(self):
        result = self.do()
        assert result == "ok"

    @pytest.mark.xfail(raises=ActionBlockedException)
    def test_exception_handler_with_ex(self):
        self.config["throw_exception"] = True
        self.do()
