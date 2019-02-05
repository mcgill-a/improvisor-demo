from flask import Flask, render_template
from flask_socketio import SocketIO, send
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile("config/defaults.py")

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
socketio = SocketIO(app)


class Example(db.Model):
    __tablename__ = 'Example'
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.Unicode)


@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + str(msg))
    send(msg, broadcast=True)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/presenter', methods=['GET'])
def presenter():
    return render_template('presenter.html')


@app.route('/controller', methods=['GET'])
def controller():
    tags = ['database', 'server', 'improvise', 'group project', 'image', 'youtube video']
    return render_template('controller.html', tags=tags)


@app.route('/live', methods=['GET'])
def live():
    return render_template('live.html')


if __name__ == '__main__':
    print("")
    print("--- --- --- --- --- --- ---")
    print("-- Improvisor Web Server --")
    print("--- --- --- --- --- --- ---")
    print("")
    socketio.run(app, port=8000)