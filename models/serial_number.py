from textwrap import wrap

from sqlalchemy import Column, String, Integer

from models.database import db


class SerialNumber(db.Model):
    id = Column(Integer, primary_key=True)
    number = Column(String(14), unique=True, nullable=False)

    def __str__(self):
        return f'{"-".join(wrap(self.number[-2], 3))} {self.number[-2:]}'
