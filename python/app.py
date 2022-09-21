from flask import abort, jsonify, request
from config import Items, items_schema, item_schema, db, app


@app.route("/spendings", methods=["GET"])
def get_spendings():
    order = request.args.get("order")
    currency = request.args.get("currency")

    if currency not in ["ALL", "USD", "HUF"]:
        return abort(403, "Not accepted currency!")

    if order not in ["date", "-date", "amount_in_huf", "-amount_in_huf"]:
        return abort(403, "Not accepted order!")

    if order == "-date":
        all_items = Items.query.order_by(Items.spent_at.desc())
    elif order == "-amount_in_huf":
        all_items = Items.query.order_by(Items.amount.desc())
    elif order == "amount_in_huf":
        all_items = Items.query.order_by(Items.amount.asc())
    elif order == "date":
        all_items = Items.query.order_by(Items.spent_at.asc())

    if currency == "USD":
        all_items = all_items.filter(Items.currency == "USD")
    elif currency == "HUF":
        all_items = all_items.filter(Items.currency == "HUF")
    results = items_schema.dump(all_items)
    return jsonify(results)


@app.route("/spendings", methods=["POST"])
def post_spendings():
    content = request.get_json(silent=True)
    if (
        "description" not in content
        or "amount" not in content
        or "currency" not in content
    ):
        return abort(404, "You have to provide correct information!")

    if content["currency"] not in ["USD", "HUF"]:
        return abort(403, "Not accepted currency!")

    if not content["description"] or not content["amount"] or not content["currency"]:
        return abort(404, "Input information is not correct!")

    items = Items(content["description"], content["amount"], content["currency"])
    db.session.add(items)
    db.session.commit()
    return item_schema.jsonify(items)
