from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome</h1>'

@app.route('/<string:username>')
def profile(username):
    return f'<h1>{username}\'s Profile</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)