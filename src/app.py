from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    print('hello_world() called')
    print('hello_world() yet another print statement4')
    print('hello_world() returning')
    return 'Hello World!'


if __name__ == '__main__':
    print('Main called #1')

    app.run(host='0.0.0.0')

    print('shutdown server')
