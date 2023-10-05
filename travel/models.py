from . import db
from datetime import datetime
from flask_login import UserMixin

# transforming into ORM classes for database


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=True)
    email = db.Column(db.String(100), index=True, nullable=False)
    # password hash stored in database (at least 255 chars long)
    password_hash = db.Column(db.String(255), nullable=False)
    # relation to call user.comment and comment.created_by
    comments = db.relationship(
        "Comment", backref="user"
    )  # backref means you can pass anything from user object into comment from id - foreign key determined


class Destination(db.Model):
    __tablename__ = "destinations"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    currency = db.Column(db.String(3))
    # ... Create the Comments db.relationship
    # relation to call destination.comments and comment.destination
    comments = db.relationship("Comment", backref="destination")

    def __repr__(self):  # string print method
        return f"<Name: {self.name}>"


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    # add the foreign key
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    destination_id = db.Column(db.Integer, db.ForeignKey("destinations.id"))

    def __repr__(self):
        return f"<Comment: {self.text}>"
