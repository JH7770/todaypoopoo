from todaypoopoo import db

class PooPoo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.String, db.ForeignKey('user.userid', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('poopoo_set'))
