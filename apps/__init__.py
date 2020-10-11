from flask import Flask
from .celery_task.celery_init import make_celery

def register_blueprints(app):
    from apps.test import test as test_blueprint
    app.register_blueprint(test_blueprint, url_prefix = '/api')

def register_plugin(app):
    from apps.models import db
    db.init_app(app)
    with app.app_context():
        db.create_all()

app = Flask(__name__)

app.config.from_object('apps.configs')
celery = make_celery(app)

register_blueprints(app)
register_plugin(app)

from .celery_task.tasks import *


