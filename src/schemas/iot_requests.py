from pydantic import BaseModel


class MeasurementRequest(BaseModel):
    iot_device: str
    measurement: str
    value: float
