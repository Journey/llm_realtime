import jwt
import os
import datetime
from typing import Optional
from backend.utils.utils.log import getLogger

secret_id: str = os.environ["ZHIPU_API_KEY"]
[secret_key, secret] = secret_id.split(".")
alogorithm = "HS256"


def authenticate(token: str) -> Optional[str]:
    """
    authenticate jwt token
    """
    getLogger().info(f"start authenticate token: {token}")
    try:
        payload = jwt.decode(token, secret, algorithms=[alogorithm])
        return payload
    except Exception as ex:
        getLogger().error(ex)
    return None


def generate_token(user: str = "anonymouse", roles: list[str] = []) -> str:
    """
    generate jwt token for a given user
    """
    payload = {
        "sub": user,
        "name": user,
        "iat": datetime.datetime.now(datetime.timezone.utc),
        "exp": datetime.datetime.now(datetime.timezone.utc)
        + datetime.timedelta(hours=1),
        "roles": roles,
    }
    token = jwt.encode(payload, secret, alogorithm)
    return token
