import datetime
import pytest
from infrastructure import badge_cache

def test_create_key():
    # Test valid userID input
    userID = '12345'
    assert badge_cache.__create_key(userID) == '12345'

    # Test empty userID input
    userID = ''
    with pytest.raises(Exception) as e:
        badge_cache.__create_key(userID)
    assert str(e.value) == "userID is required"

