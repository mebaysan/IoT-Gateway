from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class LoggingSettings(BaseSettings):
    log_level: str = "INFO"
    log_to_file: bool = False
    log_to_console: bool = True
    log_file_path: str = "myapp.log"


class AppSettings(BaseSettings):
    app_name: str = "My App"
    middleware_acceptance_header: str = "X-MY-AUTH-KEY"
    middleware_acceptance_value: str = "AC-KAPIYI-BEZIRGAN-BASI"
    public_urls: list[str] = ["/health", "/docs", "/redoc", "/openapi.json"]
    allowed_origins: list[str] = ["*"]
    https_redirect_forced: bool = False


class InfluxDBSettings(BaseSettings):
    influxdb_url: str = "http://localhost:8086"
    influxdb_bucket: str = "dev"
    influxdb_org: str = "dev"
    influxdb_token: str = "admin"


logging_settings = LoggingSettings()
app_settings = AppSettings()
influxdb_settings = InfluxDBSettings()
