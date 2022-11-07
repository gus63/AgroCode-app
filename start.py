from wsgiref.simple_server import WSGIServer
from sweater import app


def runserver():
    if __name__ == '__main__':
        app = create_app()
        app.run(debug=True, host='127.0.0.1', port=5000)
        http_server = WSGIServer(('', 5000), app)
        http_server.serve_forever()
