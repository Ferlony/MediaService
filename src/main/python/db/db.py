from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.schema import DropTable
from sqlalchemy.ext.compiler import compiles

from src.main.python.config.config_dataclass import ConfigData

engine = create_engine(f'sqlite:///{ConfigData.db_path}')
# engine = create_engine(f"postgresql+psycopg2://{ConfigData.user}:{ConfigData.password}@{ConfigData.host}/postgres")
session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)
