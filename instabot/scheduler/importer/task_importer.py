import inspect
import pkgutil
from pathlib import Path
from importlib import import_module

import instabot.scheduler


def import_tasks(package_path):
    tasks = {}
    for (_, name, _) in pkgutil.iter_modules([Path(package_path)]):
        imported_module = import_module('.' + name, package='.'
                                        .join(package_path.split('/')))
        print(imported_module)
        for i in dir(imported_module):
            attribute = getattr(imported_module, i)

            if inspect.isclass(attribute) and issubclass(attribute,
                                                         instabot.scheduler
                                                                 .Task) \
                    and not inspect.isabstract(attribute):
                tasks[attribute.task_id] = attribute

    return tasks
