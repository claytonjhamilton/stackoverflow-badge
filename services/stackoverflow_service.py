from models.validation_error import ValidationError
import httpx
from httpx import Response
from infrastructure import badge_cache


async def StackUserRequestAsync(userID: str):
    userID = validate_input(userID)

    if badge := badge_cache.get_badge(userID):
        return badge

    url = f"https://api.stackexchange.com/2.3/users/{userID}?order=desc&sort=reputation&site=stackoverflow&filter=!LnOc*f7Nq.zHgKSZ9QN_vj"

    async with httpx.AsyncClient() as client:
        resp: Response = await client.get(url)
        if resp.status_code != 200:
            raise ValidationError(resp.text, status_code=resp.status_code)

    json_data = resp.json()
    data = json_data["items"][0]

    rep = data["reputation"]
    gold = data["badge_counts"]["gold"]
    silver = data["badge_counts"]["silver"]
    bronze = data["badge_counts"]["bronze"]

    badge_cache.set_badge(
        userID, {"rep": rep, "gold": gold, "silver": silver, "bronze": bronze}
    )

    return {"rep": rep, "gold": gold, "silver": silver, "bronze": bronze}


def validate_input(userID):
    if userID.isnumeric():
        return userID
    else:
        error = f"userID is invalid. Must be an integer."
        raise ValidationError(status_code=400, error_msg=error)
