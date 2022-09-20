from email.policy import default
from typing_extensions import Required
from flask import Flask, abort, jsonify, request
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


@app.route("/spendings", methods=["GET"])
def get_spendings():
    print("GET spending")

    order = request.args.get("order")
    if order == "-date":
        all_items = Items.query.order_by(Items.spent_at.desc())
    elif order == "-amount_in_huf":
        all_items = Items.query.order_by(Items.amount.desc())
    elif order == "amount_in_huf":
        all_items = Items.query.order_by(Items.amount.asc())
    elif order == "date":
        all_items = Items.query.order_by(Items.spent_at.asc())

    currency = request.args.get("currency")
    if currency == "USD":
        all_items = all_items.filter(Items.currency == "USD")
    elif currency == "HUF":
        all_items = all_items.filter(Items.currency == "HUF")

    results = items_schema.dump(all_items)
    return jsonify(results)


@app.route("/spendings", methods=["POST"])
def post_spendings():
    print("POST spending")
    description = request.json["description"]
    amount = request.json["amount"]
    currency = request.json["currency"]
    if not description or not amount:
        return abort(404, "You have to provide a 'description' and 'amount'!")
    else:
        items = Items(description, amount, currency)
        # add items to the db
        db.session.add(items)
        # commit db
        db.session.commit()
        return item_schema.jsonify(items)
