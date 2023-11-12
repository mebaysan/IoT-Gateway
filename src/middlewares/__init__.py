from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from .auth import BaysanAuthHeaderMiddleware
from settings import app_settings

APP_MIDDLEWARES = [
    Middleware(BaysanAuthHeaderMiddleware),
    Middleware(CORSMiddleware, allow_origins=app_settings.allowed_origins),
]

if app_settings.https_redirect_forced:
    APP_MIDDLEWARES.append(Middleware(HTTPSRedirectMiddleware))
