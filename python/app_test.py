import json
from app import app


def test_post_spendings_curr():
    response = app.test_client().post(
        "/spendings",
        data=json.dumps(
            {
                "amount": 1500000,
                "currency": "CHF",
                "description": "Bérlet",
            }
        ),
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 403
    assert "Not accepted currency!" in response.data.decode("utf-8")


def test_post_spendings_missing():
    response = app.test_client().post(
        "/spendings",
        data=json.dumps(
            {
                "description": "Bérlet",
            }
        ),
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 404
    assert "You have to provide correct information!" in response.data.decode("utf-8")


def test_post_spendings_empty():
    response = app.test_client().post(
        "/spendings",
        data=json.dumps(
            {
                "amount": 0,
                "currency": "USD",
                "description": "",
            }
        ),
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 404
    assert "Input information is not correct!" in response.data.decode("utf-8")


def test_post_spendings_empty_amount():
    response = app.test_client().post(
        "/spendings",
        data=json.dumps(
            {
                "amount": 0,
                "currency": "USD",
                "description": "yep",
            }
        ),
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 404
    assert "Input information is not correct!" in response.data.decode("utf-8")
