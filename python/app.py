from flask import abort, jsonify, request
from config import Items, items_schema, item_schema, db, app


@app.route("/spendings", methods=["GET"])
def get_spendings():
    all_items = Items.query.order_by(Items.id.desc())
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
    if currency == "ALL":
        all_items = all_items.filter(Items.id > 0)
    elif currency == "USD":
        all_items = all_items.filter(Items.currency == "USD")
    elif currency == "HUF":
        all_items = all_items.filter(Items.currency == "HUF")
    results = items_schema.dump(all_items)
    return jsonify(results)


@app.route("/spendings", methods=["POST"])
def post_spendings():
    description = request.json["description"]
    amount = request.json["amount"]
    currency = request.json["currency"]
    usd = "USD"
    huf = "HUF"
    if not description or not amount:
        return abort(404, "You have to provide a 'description' and 'amount'!")
    elif currency == usd or currency == huf:
        items = Items(description, amount, currency)
        db.session.add(items)
        db.session.commit()
        return item_schema.jsonify(items)
    else:
        return abort(403, "Not accepted currency!")
