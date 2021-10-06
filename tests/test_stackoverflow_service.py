import pytest
import httpx
# import pytest_mock

from services import stackoverflow_service


def test_stackoverflow_service_active():
    """Check if URL is still active/up to date"""
    assert httpx.get("https://api.stackexchange.com/docs").status_code == 200


@pytest.fixture
def user_test_ID():
    return {"incorrectID": "a2d1d2", "correctID": "14122375"}


def test_validate_input(user_test_ID):
    """Ensure userIDs are numeric strings and fail if not"""
    with pytest.raises(Exception):
        assert stackoverflow_service.validate_input(
            user_test_ID["incorrectID"]
        )
    assert (
        stackoverflow_service.validate_input(user_test_ID["correctID"])
        == user_test_ID["correctID"]
    )
