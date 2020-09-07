import os
from flask import Flask

from jaeger_client import Config
from flask_opentracing import FlaskTracer

app = Flask(__name__)


@app.route('/')
def hello_world():
    print('hello_world() called')
    print('hello_world() yet another print statement4')
    print('hello_world() returning')
    return 'Hello World!'


def initialize_tracer():
    host = os.environ.get('REPORTING_HOST', 'localhost')
    port = os.environ.get('REPORTING_PORT', '5775')
    print(f'Initialize tracer with {host}:{port}')
    config = Config(
        config={
            'sampler': {'type': 'const', 'param': 1},
            'local_agent': {
                'reporting_host': host,
                'reporting_port': port,
            },
        },
        service_name='hello-world')
    return config.initialize_tracer()  # also sets opentracing.tracer


flask_tracer = FlaskTracer(initialize_tracer, True, app)

if __name__ == '__main__':
    print('Main called #1')

    app.run(host='0.0.0.0')

    print('shutdown server')
