from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'my_super_secure_secret_key_123')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


# Database Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    failed_attempts = db.Column(db.Integer, default=0)


# Login Route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user:

            # Account Lock Check
            if user.failed_attempts >= 3:
                flash("Account Locked. Too many failed attempts.", "danger")
                return redirect('/')

            # Password Check
            if bcrypt.check_password_hash(user.password, password):

                user.failed_attempts = 0
                db.session.commit()

                session['user_name'] = user.name
                flash('Login Successful!', 'success')
                return redirect('/dashboard')

            else:
                user.failed_attempts += 1
                db.session.commit()

                flash('Invalid Email or Password', 'danger')
                return redirect('/')

        flash('Invalid Email or Password', 'danger')
        return redirect('/')

    return render_template('login.html')


# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Check Existing Email
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash('Email already registered!', 'warning')
            return redirect('/register')

        # Hash Password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create User
        user = User(
            name=name,
            email=email,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        flash('Registration Successful! Please Login.', 'success')
        return redirect('/')

    return render_template('register.html')


# Dashboard Route
@app.route('/dashboard')
def dashboard():
    if 'user_name' not in session:
        flash('Please login first.', 'warning')
        return redirect('/')

    return render_template(
        'dashboard.html',
        name=session['user_name']
    )


# Logout Route
@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'success')
    return redirect('/')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)