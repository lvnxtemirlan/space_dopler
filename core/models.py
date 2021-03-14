from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy_mixins import AllFeaturesMixin, ReprMixin, TimestampsMixin

from .database import base, engine, session


class BaseModel(base, AllFeaturesMixin, TimestampsMixin, ReprMixin):
    __abstract__ = True

    def __init__(self, *args, **kwargs):
        pass


class Continent(BaseModel):
    __tablename__ = "continents"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255))

    countries = relationship("Country", back_populates="continent")


class Country(BaseModel):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, autoincrement=True)
    continent_id = Column(Integer, ForeignKey("continents.id"))
    name = Column(String(length=255))

    continent = relationship("Continent", back_populates="countries")


base.metadata.create_all(engine)
BaseModel.set_session(session)
