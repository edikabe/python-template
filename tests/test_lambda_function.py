from lambda_function import handler


def test_lambda_handler() -> None:
    res = handler({"data": "test"}, None)
    assert res["statusCode"] == 200
