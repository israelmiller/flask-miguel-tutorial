from app import db 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.column(db.String(64))
    email = db.Column(db.String(120))
    password_hash = db.Column(db.String(128))
    db.UniqueConstraint('username', 'email')

    def __repr__(self):
        return '<User {}>'.format(self.username)