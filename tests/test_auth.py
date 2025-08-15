def test_register_and_login_flow(client):
    # Register
    r = client.post("/api/v1/users/", json={
        "email": "u@example.com", "password": "secret", "full_name": "U"
    })
    assert r.status_code == 201, r.text

    # Login
    r2 = client.post("/api/v1/auth/login", json={
        "email": "u@example.com", "password": "secret"
    })
    assert r2.status_code == 200, r2.text
    token = r2.json()["access_token"]
    assert token
