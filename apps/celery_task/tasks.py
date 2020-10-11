from .. import celery

@celery.task
def task_test(name):
    print(name)