from sqlalchemy import Column, Integer, ForeignKey, Boolean, Text, DateTime, UnicodeText
from sqlalchemy.orm import relationship

from datetime import datetime
import pytz

import html

from scoring_engine.models.base import Base
from scoring_engine.config import config


class Persist(Base):
    __tablename__ = 'persists'
    id = Column(Integer, primary_key=True)
    round_id = Column(Integer, ForeignKey('rounds.id'))
    round = relationship('Round', back_populates='checks')
    service_id = Column(Integer, ForeignKey('services.id'))
    service = relationship('Service')
    team = Column(Integer, ForeignKey('teams.id'))
    completed_timestamp = Column(DateTime)
    completed = Column(Boolean, default=False)

    @property
    def local_completed_timestamp(self):
        completed_timezone_obj = pytz.timezone('UTC').localize(self.completed_timestamp)
        return completed_timezone_obj.astimezone(pytz.timezone(config.timezone)).strftime('%Y-%m-%d %H:%M:%S %Z')
