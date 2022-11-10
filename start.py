from sweater import app
from wsgiref.simple_server import WSGIServer


def runserver():
    if __name__ == '__main__':
        app.run(debug=False, host='0.0.0.0', port=5000)
