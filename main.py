from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/')
def main_page():
    return render_template('home.html')

# [START submitted]
@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']
    # [END submitted]
    # [START render_template]
    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        site=site,
        comments=comments)
    # [END render_template]


#socket.io app
@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcase=True)
