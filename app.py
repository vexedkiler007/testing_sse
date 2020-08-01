
from flask import Flask, Response, render_template
import sqlite3
import time
app = Flask(__name__)


def get_data():
    time.sleep(1)
    s = time.ctime(time.time())
    return s


@app.route('/')
def root():
    return render_template('client_app.html')


@app.route("/stream")
def stream():
    def eventStream():
        while True:
            yield f'data:{get_data()}\n\n'

    return Response(eventStream(), mimetype="text/event-stream")

if __name__ == '__main__':
    app.run()
