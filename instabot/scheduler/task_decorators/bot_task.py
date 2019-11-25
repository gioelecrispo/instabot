from decoripy import AbstractDecorator


class BotTask(AbstractDecorator):

    def __do_before__(self, *args, **kwargs):
        task = args[0]
        task_name = task.task_name
        bot = task.bot
        config = task.config
        bot.logger.info("TASK [STARTING] -> `{}` will be executed with "
                        "the following config: {}".format(task_name, config))

