from instabot.scheduler import import_tasks


def test_import_task():
    tasks = import_tasks('instabot/scheduler/tasks')
    assert len(tasks.keys()) != 0