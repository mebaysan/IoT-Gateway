from datetime import datetime
from influxdb_client import Point


class Measurement(object):
    table_name: str = "measurements"

    def __init__(
        self,
        iot_device: str,
        measurement: str,
        value: float,
    ) -> None:
        self.iot_device = iot_device
        self.measurement = measurement
        self.value = value
        self.measurement_ts = datetime.utcnow()

    def __repr__(self) -> str:
        return f"Measurement({self.iot_device}, {self.measurement}, {self.value}, {self.measurement_ts})"

    def __str__(self) -> str:
        return f"Measurement({self.iot_device}, {self.measurement}, {self.value}, {self.measurement_ts})"

    def to_influxdb_point(self) -> Point:
        return (
            Point(self.table_name)
            .tag("iot_device", self.iot_device)
            .tag("measurement", self.measurement)
            .field("value", self.value)
            .time(self.measurement_ts)
        )
