from models.validation_error import ValidationError


def test_ValidationError():
    ve = ValidationError(error_msg="test", status_code=400)
    assert ve.status_code == 400
    assert ve.error_msg == "test"
