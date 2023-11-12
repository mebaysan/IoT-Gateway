from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemas.iot_requests import MeasurementRequest
from models.measurement import Measurement
from helpers.influxdb2 import write_to_influxdb2

iot_router = APIRouter()


@iot_router.post("/measure")
async def measure(iot_measurement_request: MeasurementRequest):
    measurement = Measurement(
        iot_measurement_request.iot_device,
        iot_measurement_request.measurement,
        iot_measurement_request.value,
    )
    if write_to_influxdb2(
        measurement.to_influxdb_point(),
    ):
        return JSONResponse(
            status_code=200,
            content={"status": "ok", "message": "Measurement processed successfully!"},
        )
    else:
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": "Error while processing measurement!",
            },
        )
