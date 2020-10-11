from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, DateTime

db = SQLAlchemy()


class Article(db.Model):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), unique=True, default='')
    desc = Column(String(255), default='')
    content = Column(String(50), default='')
    author = Column(String(11), default='')
    classify = Column(String(50), default='')
    se_classify = Column(String(50), default='')
    image = Column(String(50), default='')
    view = Column(Integer, default=0)
    date = Column(DateTime, default=datetime.now)