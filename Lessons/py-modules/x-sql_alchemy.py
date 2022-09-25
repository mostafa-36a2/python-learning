from urllib.parse import quote

from sqlalchemy import (
    VARCHAR,
    BigInteger,
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

DB_RAP_USER = "rap"
DB_RAP_PASSWORD = "CC8VEKKmU0c*pM4p"

DB_HOST = "192.168.127.30"
DB_PORT = "33306"

rap_db_connection_string = (
    f"mysql+pymysql://{DB_RAP_USER}:%s@{DB_HOST}:{DB_PORT}/playground"
    % quote(DB_RAP_PASSWORD)
)

engine = None
Base = declarative_base()


def get_engine(echo_value=False):
    global engine
    if engine:
        return engine
    try:
        print("Creating sqlalchemy engine...")
        engine = create_engine(rap_db_connection_string, echo=echo_value)
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(
            f"Unexpected Failure in creating engine! <Probably connection failed {e}>."
        )
        return None
    return engine


################################################################
################################################################
################################################################


def show_tables():
    try:
        metadata = MetaData()
        metadata.reflect(bind=engine)
    except Exception as e:
        print(f"Show tables failed, probably no connection, exception is {e}")
        exit()
    print(metadata.tables)


def drop_table(table_name, engine):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = metadata.tables[table_name]
    if table is not None:
        Base.metadata.drop_all(engine, [table], checkfirst=True)


def add(objects_list):
    # create session and add objects
    # session.connection().connection
    with Session(get_engine(False)) as session:
        with session.begin():  # Returns SessionTransaction object
            for object in objects_list:
                session.add(object)
        # inner context calls session.commit(), if there were no exceptions
        # outer context calls session.close()
    return True


class User(Base):
    __tablename__ = "user"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(16), unique=True)
    address = Column("address", VARCHAR(16), unique=True)
    balance = Column("balance", BigInteger, unique=True)
    birthdate = Column("birthdate", DateTime, unique=True)


# Connection details
engine = get_engine(False)
drop_table("user", engine)
assert engine, "No engine to work out"
print(engine)
show_tables()
