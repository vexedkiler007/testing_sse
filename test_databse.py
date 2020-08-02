import sqlite3
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, text


def create_rules_table(name):
    conn = sqlite3.connect(f'{name}.sqlite')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE Rules (id TEXT, author TEXT, rule TEXT)""")


def insert_data():
    conn = sqlite3.connect("test.sqlite")
    cur = conn.cursor()
    cur.execute("""INSERT INTO Rules (id, author, rule) values("2", "Sarah", "This is cool rule")""")
    conn.commit()


def test_sqlite3():
    create_rules_table('test')
    for _ in range(0, 10):
        insert_data()


engine = sqlalchemy.create_engine("mysql+mysqldb://root:@localhost/cool_rules")
Base = declarative_base()


class Rules(Base):
    __tablename__ = 'Rules'

    id = Column(Integer, primary_key=True)
    author = Column(String(256))
    rule = Column(String(256))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.id, self.author, self.rule)


Base.metadata.create_all(engine)


