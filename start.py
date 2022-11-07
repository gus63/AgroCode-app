from sweater import app, db
from wsgiref.simple_server import WSGIServer


def runserver():
    if __name__ == '__main__':
        with app.app_context():
            db.create_all()
        app.run(debug=True, host='127.0.0.1', port=5000)
    #   http_server = WSGIServer(('', 5000), app)
    #   http_server.serve_forever()
