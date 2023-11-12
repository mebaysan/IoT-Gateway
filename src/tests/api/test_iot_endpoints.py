import pytest


def test_endpoint_measure(client, headers, mocker):
    """Tests the measure endpoint."""
    data = {
        "iot_device": "farm_1",
        "measurement": "temperature",
        "value": 23.5,
    }

    mocker.patch("helpers.influxdb2.write_to_influxdb2", return_value=True)

    response = client.post(
        "iot/measure",
        json=data,
        headers=headers,
    )
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "message": "Measurement processed successfully!",
    }


@pytest.mark.skip
def test_endpoint_measure_fail(client, headers, mocker):
    """Tests the measure endpoint to fail."""
    data = {
        "iot_device": "farm_1",
        "measurement": "temperature",
        "value": 23.5,
    }
    # todo: this should be fixed
    mocker.patch("helpers.influxdb2.write_to_influxdb2", return_value=False)

    response = client.post(
        "iot/measure",
        json=data,
        headers=headers,
    )

    assert response.status_code == 400
    assert response.json() == {
        "status": "error",
        "message": "Error while processing measurement!",
    }
