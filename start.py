from sweater import app


def runserver():
    if __name__ == '__main__':
        app = create_app()
        app.run(Flask_debug=True, host='0.0.0.0', port=5000)
