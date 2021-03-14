import pymysql
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from settings import DB_LINK

pymysql.install_as_MySQLdb()
engine: sqlalchemy.engine.base.Engine = create_engine(DB_LINK)
session: sqlalchemy.orm.scoped_session = scoped_session(sessionmaker(bind=engine, autocommit=True))

base = declarative_base()
