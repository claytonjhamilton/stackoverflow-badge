import pytest

# import pytest_mock
import httpx
from services import stackoverflow_service


def test_stackoverflow_service_active():
    """Check if URL is still active/up to date"""
    assert httpx.get("https://api.stackexchange.com/").status_code == 200


def test_validate_input():
    """Ensure userIDs are numeric strings and fail if not"""
    userID = {"incorrectID": "a2d1d2", "correctID": "14122375"}
    with pytest.raises(Exception):
        assert stackoverflow_service.validate_input(userID["incorrectID"])
    assert (
        stackoverflow_service.validate_input(userID["correctID"]) == userID["correctID"]
    )


# def mock_response_object(code):
#     resp = requests.Response()
#     resp.status_code = code
#     return resp
