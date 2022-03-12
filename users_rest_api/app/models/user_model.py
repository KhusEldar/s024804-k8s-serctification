from db import db


class UserModel(db.Model):
    """Model of a user from database"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"id = {self.id}, first_name = {self.firstname}, last_name = {self.lastname}, age = {self.age}"
