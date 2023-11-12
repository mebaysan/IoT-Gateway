import random
import httpx

BASE_URL = "http://localhost:8080"
HEADERS = {"X-MY-AUTH-KEY": "AC-KAPIYI-BEZIRGAN-BASI"}

IOT_DEVICE_LIST = ["device_1", "device_2", "device_3"]
MEASUREMENT_NAME_LIST = ["temperature", "humidity", "pressure"]


def make_request(method, endpoint, json=None):
    return httpx.request(method, BASE_URL + endpoint, json=json, headers=HEADERS)


# response_health = make_request("GET", "/health")

# print(response_health.json())


# data = {
#     "iot_device": "farm_1",
#     "measurement": "temperature",
#     "value": 23.5,
# }
# response_measurement = make_request("POST", "/measure", json=data)

# print(response_measurement.json())


# generate a function to generate a random data
def generate_data():
    return {
        "iot_device": random.choice(IOT_DEVICE_LIST),
        "measurement": random.choice(MEASUREMENT_NAME_LIST),
        "value": random.uniform(0, 100),
    }


while True:
    data = generate_data()
    try:
        response_measurement = make_request("POST", "/iot/measure", json=data)
        print(response_measurement.json())
    except Exception as e:
        print(e)
