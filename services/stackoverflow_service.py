import httpx
from httpx import Response
from infrastructure import badge_cache

from models.validation_error import ValidationError


def validate_input(userID):
    if userID.isnumeric():
        return userID
    raise ValidationError(
        status_code=400, error_msg="userID is invalid. Must be an integer."
    )


def format_api_output(response):
    """Format retrieved json from API call"""
    data = response["items"][0]
    return {
        "rep": data["reputation"],
        "gold": data["badge_counts"]["gold"],
        "silver": data["badge_counts"]["silver"],
        "bronze": data["badge_counts"]["bronze"],
    }


async def StackUserRequestAsync(userID: str):
    userID = validate_input(userID)

    if badge := badge_cache.get_badge(userID):
        return badge

    url = f"https://api.stackexchange.com/2.3/users/{userID}?order=desc&sort=reputation&site=stackoverflow&filter=!LnOc*f7Nq.zHgKSZ9QN_vj"

    async with httpx.AsyncClient() as client:
        resp: Response = await client.get(url)
        if resp.status_code != 200:
            raise ValidationError(resp.text, status_code=resp.status_code)

    formatted_data = format_api_output(resp.json())

    badge_cache.set_badge(userID, formatted_data)

    return formatted_data
