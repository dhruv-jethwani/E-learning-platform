from flask import Blueprint, render_template, request, flash, redirect, url_for,session
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        role = str.lower(request.form.get('role'))
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user.email == email and user.password == password and user.role == role:
            name = user.full_name
            role_user = role
            flash('Logged in successfully!', category='success')
            if role == 'student':
                return redirect(url_for('views.dash'))
            elif role == 'teacher':
                return redirect(url_for('views.teacher'))
            else:
                return redirect(url_for('views.admin'))
        else:
            flash('Invalid email or role or password.', category='error')

    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.pop('user_id', None)  # Clear user ID from session
    flash('Logged out successfully!', category='success')
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        role = str.lower(request.form.get('role'))
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if password1 != password2:
            flash('Passwords do not match.', category='error')
        elif email.count('@') == 0:
            flash("Email should contain '@'.", category='error')
        elif len(phone) != 10:
            flash('Phone Number should be 10 digits.', category='error')
        elif len(password1) < 8 or len(password1) > 14:
            flash('Password should be between 8 to 14 characters.', category='error')
        elif role not in ['admin','teacher','student']:
            flash('Invalid role written', category='error')
        else:
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                flash('Email already exists.', category='error')
            else:
                new_user = User(full_name=full_name, phone=phone, email=email,role=role, password=password1)
                db.session.add(new_user)
                db.session.commit()
                flash('Account successfully created. You can now log in.', category='success')
                return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth.route('/CS', methods=['POST'])
def CS():
    return render_template('CS.html')

@auth.route('/AI', methods=['POST'])
def AI():
    return render_template('AI.html')
