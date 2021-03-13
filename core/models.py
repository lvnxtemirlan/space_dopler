from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy_mixins import AllFeaturesMixin

from .database import base, session


class BaseModel(base, AllFeaturesMixin):
    __abstract__ = True


class Continents(BaseModel):
    __tablename__ = "continents"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255))


class Countries(BaseModel):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True, autoincrement=True)
    continent_id = Column(Integer, ForeignKey("continents.id"))
    name = Column(String(length=255))


BaseModel.set_session(session)


Countries.create(continent_id=5).add()

Countries().fill(contient_id=45)