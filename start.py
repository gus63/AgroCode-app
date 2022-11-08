from sweater import app, db
from wsgiref.simple_server import WSGIServer


def runserver():
    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
  #      with app.app_context():
  #          db.create_all()

    #   http_server = WSGIServer(('', 5000), app)
    #   http_server.serve_forever()
