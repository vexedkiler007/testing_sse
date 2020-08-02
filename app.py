import json
import sqlalchemy
from flask import Flask, Response, render_template
import time
app = Flask(__name__)


def get_data():
    engine = sqlalchemy.create_engine("mysql+mysqldb://root@localhost/cool_rules")
    with engine.connect() as connection:
        result = connection.execute("SELECT * FROM Rules")
        time.sleep(10)
    return json.dumps([(row['author'], row['rule']) for row in result])


@app.route('/')
def root():
    engine = sqlalchemy.create_engine("mysql+mysqldb://root@localhost/cool_rules")
    with engine.connect() as connection:
        result = connection.execute("SELECT * FROM Rules")
    result_ = [(row['author'], row['rule']) for row in result]
    print(len(result_))
    return render_template('client_app.html', result= result_, result_len=len(result_))


@app.route("/stream")
def stream():

    def eventStream():
        while True:
            yield f'data:{get_data()}\n\n'

    return Response(eventStream(), mimetype="text/event-stream")


if __name__ == '__main__':
    app.run()
