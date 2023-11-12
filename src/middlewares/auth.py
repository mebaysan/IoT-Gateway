from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from settings import app_settings
from helpers.logger import get_logger

logger = get_logger("middlewares")


class BaysanAuthHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: callable):
        if request.url.path in app_settings.public_urls:
            return await call_next(request)
        if (
            request.headers.get(app_settings.middleware_acceptance_header)
            == app_settings.middleware_acceptance_value
        ):
            response = await call_next(request)
            response.headers[
                app_settings.middleware_acceptance_header
            ] = app_settings.middleware_acceptance_value
            return response
        else:
            logger.warning(
                "Unauthorized request to endpoint %s from %s",
                request.url.path,
                request.client.host,
            )
            return JSONResponse(
                content={
                    "status": "error",
                    "message": "You can not access this endpoint",
                },
                status_code=403,
            )
