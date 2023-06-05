from app import db
from app.models.user import User
from datetime import datetime

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(200))
    title = db.Column(db.String(100))
    price = db.Column(db.Integer)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)

    user = db.relationship('User', backref='products')


    def serialize(self):
        return {
            'id': self.id,
            'image_url': self.image_url,
            'title': self.title,
            'price': self.price,
            'description': self.description,
            'created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            'updated_at': self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
            'user': self.user.serialize()
        }