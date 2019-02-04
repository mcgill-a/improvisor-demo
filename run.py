from flask import Flask, render_template
from flask_socketio import SocketIO, send
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

bootstrap = Bootstrap(app)
socketio = SocketIO(app)

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


if __name__ == '__main__':
    print("")
    print("--- --- --- --- --- --- ---")
    print("-- Improvisor Web Server --")
    print("--- --- --- --- --- --- ---")
    print("- Connected: SocketIO")
    print("- Connected: MySQL Database")
    print("--- --- --- --- --- --- ---")
    print("")
    socketio.run(app, port=8000)