from flask import Flask, render_template, request, redirect, url_for, flash, session
from util.exts import db
from util.models import *
from util.hasher import Hasher
from util.formater import Formater
from util.emailer import Emailer
import config


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return redirect(url_for('home_page'))


@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/subject')
def subject_page():
    if session.get('username') is not None:
        subjects = Subject.query.filter(
            Subject.account_id == session.get('account_id')).all()
        return render_template('subject.html', subjects=subjects)
    else:
        return redirect(url_for('user_page'))


@app.route('/subject/<number>')
def subject_profile(number):
    if session.get('username') is not None:
        subject = Subject.query.filter(Subject.account_id == session.get(
            'account_id'), Subject.number == number).first()
        elements = Element.query.filter(Element.account_id == session.get(
            'account_id'), Element.subject_no == number).all()
        return render_template('subject_profile.html', subject=subject, elements=elements)
    else:
        return redirect(url_for('user_page'))


@app.route('/subject', methods=['POST'])
def new_subject():
    if session.get('username') is not None:
        data = request.form
        number = len(Subject.query.filter(
            Subject.account_id == session.get('account_id')).all())
        name = data.get('new_subject_name')
        new_subject = Subject(account_id=session.get(
            'account_id'), number=number, name=name)
        db.session.add(new_subject)
        db.session.commit()
        return redirect(url_for('subject_page'))
    else:
        return redirect(url_for('user_page'))


@app.route('/subject/<number>/update', methods=['POST'])
def update_subject(number):
    if session.get('username') is not None:
        data = request.form
        subject = Subject.query.filter(Subject.account_id == session.get(
            'account_id'), Subject.number == number).first()
        name = data.get('update_subject_name')
        subject.name = name
        db.session.commit()
        return redirect(url_for('subject_page'))
    else:
        return redirect(url_for('user_page'))


@app.route('/element/<number>')
def element_profile(number):
    if session.get('username') is not None:
        element = Element.query.filter(Element.account_id == session.get(
            'account_id'), Element.number == number).first()
        return render_template('element_profile.html', element=element)
    else:
        return redirect(url_for('user_page'))


@app.route('/element', methods=['POST'])
def new_element():
    if session.get('username') is not None:
        data = request.form
        number = len(Element.query.filter(
            Element.account_id == session.get('account_id')).all())
        subject_no = data.get('subject_no')
        name = data.get('new_element_name')
        description = data.get('description')
        new_element = Element(account_id=session.get(
            'account_id'), number=number, subject_no=subject_no, name=name, description=description)
        db.session.add(new_element)
        db.session.commit()
        return redirect(url_for('subject_page'))
    else:
        return redirect(url_for('user_page'))


@app.route('/element/<number>/update', methods=['POST'])
def update_element(number):
    if session.get('username') is not None:
        data = request.form
        element = Element.query.filter(Element.account_id == session.get(
            'account_id'), Element.number == number).first()
        original_number = element.subject_no
        subject_no = data.get('update_element_subject_no')
        name = data.get('update_element_name')
        description = data.get('update_element_description')
        element.name = name
        element.subject_no = subject_no
        element.description = description
        db.session.commit()
        return redirect(url_for('subject_profile', number=original_number))
    else:
        return redirect(url_for('user_page'))


@app.route('/history')
def history_page():
    if session.get('username') is not None:
        return render_template('history.html')
    else:
        return redirect(url_for('user_page'))


@app.route('/log')
def log_page():
    if session.get('username') is not None:
        return render_template('log.html')
    else:
        return redirect(url_for('user_page'))


@app.route('/user')
def user_page():
    if session.get('username') is not None:
        return redirect(url_for('user_profile', username=session.get('username')))
    else:
        return render_template('user.html')


@app.route('/user/<username>')
def user_profile(username):
    if username == session.get('username'):
        account = Account.query.filter(
            Account.id == session.get('account_id')).first()
        subjects = Subject.query.filter(
            Subject.account_id == session.get('account_id')).all()
        elements = Element.query.filter(
            Element.account_id == session.get('account_id')).all()
        return render_template('user_profile.html', account=account, subjects=subjects, elements=elements)
    else:
        return redirect(url_for('user_page'))


# user sign up flow
# success -> send an email with account certification -> user_page
# fail -> alert error message -> user_page
@app.route('/user/signup', methods=['POST'])
def signup():
    # data = {'signup_email': <String>, 'signup_username': <String>, 'signup_password': <String>}
    data = request.form
    account_email = Account.query.filter(
        Account.email == data.get('signup_email')).first()
    account_username = Account.query.filter(
        Account.username == data.get('signup_username')).first()

    if not (data.get('signup_email') and data.get('signup_username') and data.get('signup_password')):
        flash('Input must not be empty.', 'danger')
    elif account_email or account_username:
        flash('Email or Username has been used.', 'danger')
    elif Formater.is_email(data.get('signup_email')) is None:
        flash('Wrong email format. E.g. example@example.com', 'danger')
    else:
        while True:
            id = Hasher.hash(6)
            account_id = Account.query.filter(Account.id == id).first()
            if account_id is None:
                break
        email = data.get('signup_email')
        username = data.get('signup_username')
        password = Hasher.sha256(data.get('signup_password'))
        permission = -1
        new_account = Account(
            id=id, email=email, username=username, password=password, permission=permission)

        db.session.add(new_account)
        db.session.commit()

        Emailer.send_certificattion(
            email, id, Hasher.generate_certification(id))
        flash('Please check your email then certificate your account.', 'success')

    return redirect(url_for('user_page'))


# user sign in flow (activated permission)
# success -> redirect to user_profile page and store user information in session -> user_profile
# fail -> alert error message -> user_page
@app.route('/user/signin', methods=['POST'])
def signin():
    # data = {'signin_username': <String>, 'signin_password': <String>}
    data = request.form
    account = Account.query.filter(
        Account.username == data.get('signin_username')).first()
    if account is not None:
        if Hasher.sha256(data.get('signin_password')) == account.password:
            if account.permission >= 0:
                session['username'] = data.get('signin_username')
                session['account_id'] = account.id
            else:
                flash(
                    'Invalid Account Certification! Please check your email, then activate the account certification.', 'danger')
        else:
            flash('Account not exist! Please check your Username or Password.', 'danger')
    else:
        flash('Account not exist! Please check your Username or Password.', 'danger')

    return redirect(url_for('user_page'))


@app.route('/user/signout')
def signout():
    session.clear()
    return redirect(url_for('user_page'))


# certificate user's account by email link
# success -> permission change to 0 -> user_page
# fail -> alert error message -> user_page
@app.route('/certificate/<account_id>/<certification>')
def certificate(account_id, certification):
    check = Hasher.generate_certification(account_id)
    if certification == check:
        account = Account.query.filter(Account.id == account_id).first()
        if account is not None:
            account.permission = 0
            db.session.commit()

            flash(
                'Your account is certificated successfully. Please sign in and have a good day ~', 'success')
        else:
            flash('Account not exist! Please contact the customer service.', 'danger')
    else:
        flash('Wrong certification! Please check your email again or contact the customer service.', 'danger')

    return redirect(url_for('user_page'))


if __name__ == '__main__':
    app.run()
