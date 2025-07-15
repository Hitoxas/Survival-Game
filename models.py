from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Player(db.Model):
    __tablename__ = "Player Inventory"
    id = db.Column(db.Integer, primary_key=True)
    fiber = db.Column(db.Integer, default=0)
    sticks = db.Column(db.Integer, default=0)
    stones = db.Column(db.Integer, default=0)
    rope = db.Column(db.Integer, default=0)
    wooden_handles = db.Column(db.Integer, default=0)