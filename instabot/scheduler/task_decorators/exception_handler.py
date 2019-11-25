from decoripy import AbstractDecorator
from ..exceptions import ActionBlockedException


class ExceptionHandler(AbstractDecorator):

    def __do__(self, *args, **kwargs):
        task = args[0]
        task_name = task.task_name
        bot = task.bot
        try:
            return self.function(task)
        except ActionBlockedException as e:
            bot.logger.info("TASK [STOPPED] -> `{}` has stopped because"
                            " of {}".format(task_name, e.__cause__))

