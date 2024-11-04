from backend.auth.auth.auth import authenticate, generate_token


def test_generate_token():
    token = generate_token("haha")
    assert token is not None


def test_authenticate():
    token = generate_token("journey")
    payload = authenticate(token)
    assert isinstance(payload, dict)
    assert payload["name"] == "journey"
