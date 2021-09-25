import requests


def StackUserRequest(userID: str):
    url = f"https://api.stackexchange.com/2.3/users/{userID}?order=desc&sort=reputation&site=stackoverflow&filter=!LnOc*f7Nq.zHgKSZ9QN_vj"
    resp = requests.get(url)
    resp.raise_for_status()
    json_data = resp.json()
    data = json_data["items"][0]
    rep = str(data["reputation"])
    gold = str(data["badge_counts"]["gold"])
    silver = str(data["badge_counts"]["silver"])
    bronze = str(data["badge_counts"]["bronze"])
    return {"rep": rep, "gold": gold, "silver": silver, "bronze": bronze}
