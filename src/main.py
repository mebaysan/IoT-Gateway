from fastapi import FastAPI
from settings import app_settings
from helpers.logger import get_logger
from middlewares import APP_MIDDLEWARES
from routers.iot import iot_router


logger = get_logger("main")

app = FastAPI(
    middleware=APP_MIDDLEWARES,
    title=app_settings.app_name,
    summary="IoT Gateway",
    version="1.0",
)

app.include_router(iot_router, prefix="/iot", tags=["iot"])


@app.get("/health", status_code=200)
async def healthcheck():
    logger.info("Healthcheck endpoint called")
    return {
        "status": "ok",
        "message": "App is healthy!",
        "app_name": app_settings.app_name,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
