from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))

    def __repr__(self):
        return '<User %r>' % self.username
