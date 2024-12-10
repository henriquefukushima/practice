from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/index')
def welcome():
    return 'Welcome to the index page!'

if __name__ == '__main__':
    app.run(debug=True)