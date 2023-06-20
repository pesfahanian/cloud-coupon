from uuid import uuid4


def generate_unique_code() -> str:
    return uuid4().hex.upper()[:6]
