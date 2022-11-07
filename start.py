from sweater import app
from wsgiref.simple_server import WSGIServer


def runserver():
    if __name__ == '__main__':
        app = create_app()
        app.app_context().push()
        app.run(debug=True, host='0.0.0.0', port=80)
    #   http_server = WSGIServer(('', 5000), app)
    #   http_server.serve_forever()
