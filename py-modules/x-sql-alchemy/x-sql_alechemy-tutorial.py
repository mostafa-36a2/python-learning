# https://www.sqlalchemy.org/
# https://www.youtube.com/watch?v=NuDSWGOcvtg
import os

from sqlalchemy import Column, Integer, String, and_, create_engine, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeMeta, sessionmaker

db_dir = os.path.dirname(__file__)

engine = create_engine(f"sqlite:///{db_dir}/sqlalchemy.sqlite", echo=False)

# Map classes with tables
Base: type = declarative_base()


class users(Base):

    __tablename__ = "users"

    column1 = Column(Integer, primary_key=True, autoincrement=True)
    column2 = Column(String)
    column3 = Column(String)

    def __init__(self, val1, val2, val3) -> None:
        self.column2 = val2
        self.column3 = val3

    def __repr__(self):
        return f"{self.column1}-{self.column2}-{self.column3}"


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "insert":
    user1 = users(1, 999, 111)
    user2 = users(7, 444, 222)
    user3 = users(8, 555, 333)

    session.add(user1)
    session.add(user2)
    session.add(user3)

    session.add_all([user1, user2, user3])
    session.commit()

if __name__ == "__main__":

    res = session.query(users).limit(5)
    print("\n.all()", "-" * 40)
    print("*" * 80)
    for row in res:
        print(row)

    print("\nfilter(users.column1>10,users.column2<10):", "-" * 40)
    print("*" * 80)
    res = session.query(users).filter(users.column1 > 10, users.column2 < 10).limit(5)
    for row in res:
        print(row)

    print("\norder_by(users.column2):", "-" * 40)
    print("*" * 80)
    res = session.query(users).order_by(users.column2).limit(5)
    for row in res:
        print(row)

    print("\nsession.query(users).filter(users.column2>5).offset(1).limit(1)")
    print("*" * 80)
    res = session.query(users).filter(users.column2 > 5).offset(1).limit(1)
    for row in res:
        print(row)

    # https://docs.sqlalchemy.org/en/14/core/sqlelement.html#sqlalchemy.sql.expression.and_
    print("using or_")
    print("*" * 80)
    res = (
        session.query(users)
        .filter(or_(users.column2 == 1, users.column2 == 9))
        .order_by(users.column3.desc(), users.column1.asc())
        .offset(2)
        .limit(2)
    )
    for row in res:
        print(row)

    print("query, change, commit")
    print("*" * 80)
    res = session.query(users).filter().order_by(users.column1.asc()).limit(3)

    print("len:", res.count())
    for element in res:
        # change
        element.column2 = 23
        element.column3 = 44
        print(f"Element changing: {element}")
    # commit!
    session.commit()

    res = session.query(users).filter(and_(users.column2 == 23, users.column3 == 44))
    print(list(res))

    # add, select, update, delete
    session.add(users(0, 123, 123))
    user = (
        session.query(users).filter(users.column2 == 123, users.column3 == 123).first()
    )
    print(f"user added is: {user}")
    user.column3 = 987
    user.column2 = 124
    session.commit()

    user = session.query(users).filter(users.column2 == 124).first()
    print(f"user modified is: {user}")

    session.delete(user)
    res = session.commit()

    elements = session.query(users).filter(users.column2 == 124)
    print("After delete", type(elements), elements.count())
