from . import test
from ..celery_task import tasks

@test.route('/test', methods=['GET'])
def test():
    tasks.task_test.delay('zhangs')
    return {'a': 1}
