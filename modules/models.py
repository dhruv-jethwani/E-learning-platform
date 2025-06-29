from . import db 

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(100))
    phone = db.Column(db.String(15))
    email = db.Column(db.String(100), unique = True)
    role = db.Column(db.String(20))
    password = db.Column(db.String(30))
