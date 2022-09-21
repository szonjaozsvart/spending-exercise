from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql://szonja:tollTarto_2022@localhost/playing_around"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100))
    amount = db.Column(db.Integer)
    currency = db.Column(db.String(100))
    spent_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, description, amount, currency):
        self.description = description
        self.amount = amount
        self.currency = currency


class ItemSchema(ma.Schema):
    class Meta:
        fields = ("id", "description", "amount", "currency", "spent_at")


item_schema = ItemSchema()
items_schema = ItemSchema(many=True)
