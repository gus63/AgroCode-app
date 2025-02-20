from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from sweater import app, db
from sweater.models import User


@property
def password(self):
    raise AttributeError('password is not a readable attribute')


@password.setter
def password(self, password):
    self.password_hash = generate_password_hash(password)


def verify_password(self, password):
    return check_password_hash(self.password_hash, password)


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html')


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
    return render_template('analytics.html')


@app.route('/admin/', methods=['GET'])
@login_required
def admin():
    return render_template('admin/admin.html')


@app.route('/profile-map/', methods=['GET'])
@login_required
def profile_map():
    return render_template('clients-admin/profile-map.html')


@app.route('/contacts', methods=['GET'])
def contacts():
    return render_template('contacts.html')


@app.route('/password-reset', methods=['GET', 'POST'])
def psw_reset():

    return render_template('password-reset.html')


@app.route('/policy', methods=['GET', 'POST'])
def policy():

    return render_template('docs/privacy-policy.html')


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
                    next_page = request.args.get('clients-admin/profile-map.html')
                    return redirect(url_for('profile_map'))
                else:
                    flash('Логин или пароль не верный!')
            else:
                flash('Пожалуйста заполните все поля!')
    return render_template('register.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


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


