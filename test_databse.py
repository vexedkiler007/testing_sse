import sqlite3


def create_rules_table(name):
    conn = sqlite3.connect(f'{name}.sqlite')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE Rules (id TEXT, author TEXT, rule TEXT)""")


def insert_data():
    conn = sqlite3.connect("test.sqlite")
    cur = conn.cursor()
    cur.execute("""INSERT INTO Rules (id, author, rule) values("1", "David", "This is cool rule")""")
    conn.commit()


create_rules_table('test')
for _ in range(0, 10):
    insert_data()
