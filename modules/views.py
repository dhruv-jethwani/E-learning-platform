from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('register.html')

@views.route('/home')
def dash():
    return render_template('home.html')

@views.route('/admin')
def admin():
    return render_template('admin_page.html')

@views.route('/teacher')
def teacher():
    return render_template('teacher_dash.html')
