def test_endpoint_healthcheck(client, app_settings):
    """Tests the healthcheck endpoint."""
    response = client.get("health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "message": "App is healthy!",
        "app_name": app_settings.app_name,
    }


def test_unauthorized_request(client):
    """Tests the measure endpoint."""
    data = {
        "iot_device": "farm_1",
        "measurement": "temperature",
        "value": 23.5,
    }
    response = client.post(
        "iot/measure",
        json=data,
    )
    assert response.status_code == 403
    assert response.json() == {
        "status": "error",
        "message": "You can not access this endpoint",
    }
