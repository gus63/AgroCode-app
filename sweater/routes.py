from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from sweater import app
from sweater.models import Message, User


@property
def password(self):
    raise AttributeError('password is not a readable attribute')


@password.setter
def password(self, password):
    self.password_hash = generate_password_hash(password)


def verify_password(self, password):
    return check_password_hash(self.password_hash, password)


@app.route('/', methods=['GET'])
def home():
    return 'hello !!!!!!!'
    return render_template('index.html')


@app.route('/nav', methods=['GET'])
def nav_bar():
    title = "AgroCode - You agro management"
    return render_template('layouts/nav-bar.html', title=title)


@app.route('/team', methods=['GET'])
def team():
    return render_template('team.html')


@app.route('/products', methods=['GET'])
def products():
    return render_template('products.html')


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/analytic', methods=['GET'])
def analytic():
    return render_template('analytic.html')


@app.route('/admin', methods=['GET'])
def admin():
    return render_template('admin.html')


@app.route('/chart-flot', methods=['GET'])
def chart_flot():
    return render_template('chart-flot.html')


@app.route('/chart-morris', methods=['GET'])
def chart_morris():
    return render_template('chart-morris.html')


@app.route('/main', methods=['GET'])
@login_required
def main():
    return render_template('main.html', messages=Message.query.all())


@app.route('/add_message', methods=['POST'])
@login_required
def add_message():
    text = request.form['text']
    tag = request.form['tag']

    db.session.add(Message(text, tag))
    db.session.commit()

    return redirect(url_for('main'))


@app.route('/password-reset', methods=['GET', 'POST'])
def psw_reset():

    return render_template('password-reset.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    email = request.form.get('email')
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    logname = request.form.get('logname')
    logpass = request.form.get('logpass')
    logemail = request.form.get('logemail')
    check = request.form.get('reg-log')
    if check == 'on':
        if request.method == 'POST':
            if not (email or login or password or password2):
                flash('Пожалуйста, заполните все поля!')
            elif password != password2:
                flash('Пароль не совпадает!')
            else:
                hash_pwd = generate_password_hash(password)
                new_user = User(login=login, password=hash_pwd, email=email)
                db.session.add(new_user)
                db.session.commit()
    else:
        if request.method == 'POST':
            if logname and logpass and logemail:
                user = User.query.filter_by(login=logname).first()

                if user and check_password_hash(user.password, logpass):
                    login_user(user)
                    next_page = request.args.get('admin')
                    return redirect('admin')
                else:
                    flash('Логин или пароль не верный!')
            else:
                flash('Пожалуйста заполните все поля!')
    return render_template('register.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('hello_world'))


@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('register') + '?next=' + request.url)

    return response


# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("layouts/404.html"), 404


# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("layouts/500.html"), 500


