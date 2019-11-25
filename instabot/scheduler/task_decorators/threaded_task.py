import threading
from decoripy import AbstractDecorator


class ThreadedTask(AbstractDecorator):

    def __do__(self, *args, **kwargs):
        task = args[0]
        task_name = task.task_name
        bot = task.bot
        bot.logger.info("TASK [STARTING] -> `{}` will be "
                        "run threaded...".format(task_name))
        job_thread = threading.Thread(target=self.function, args=(task,))
        job_thread.start()
        return job_thread

