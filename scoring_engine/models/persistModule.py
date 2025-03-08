from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship

from scoring_engine.models.base import Base


class PersistModule(Base):
    __tablename__ = "persistDetails"
    id = Column(Integer, primary_key=True)
    persist_env = Column(Integer, ForeignKey('environments.id'))
    environment = relationship("Environment")
    properties = relationship('Property', back_populates="environment")
