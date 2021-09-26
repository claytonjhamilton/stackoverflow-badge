import datetime
from typing import Optional, Tuple

__cache = {}
cached_item_lifetime_in_hours = 1.0


def get_badge(userID) -> Optional[dict]:
    key = __create_key(userID)
    data: dict = __cache.get(key)
    if not data:
        return None

    last = data['time']
    dt = datetime.datetime.now() - last
    if dt / datetime.timedelta(minutes=60) < cached_item_lifetime_in_hours:
        return data['value']

    del __cache[key]
    return None


def set_badge(userID: str, value: dict):
    key = __create_key(userID)
    data = {
        'time': datetime.datetime.now(),
        'value': value
    }
    __cache[key] = data
    __clean_out_of_date()


def __create_key(userID: str,) -> Tuple[str]:
    if not userID:
        raise Exception("userID is required")
    return userID


def __clean_out_of_date():
    for key, data in list(__cache.items()):
        dt = datetime.datetime.now() - data.get('time')
        if dt / datetime.timedelta(minutes=60) > cached_item_lifetime_in_hours:
            del __cache[key]
