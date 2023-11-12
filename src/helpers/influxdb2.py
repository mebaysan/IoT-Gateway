import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
from settings import influxdb_settings
from helpers.logger import get_logger

logger = get_logger("influxdb2")


def write_to_influxdb2(record: influxdb_client.Point):
    try:
        client = influxdb_client.InfluxDBClient(
            url=influxdb_settings.influxdb_url,
            token=influxdb_settings.influxdb_token,
            org=influxdb_settings.influxdb_org,
        )

        write_api = client.write_api(write_options=SYNCHRONOUS)
        write_api.write(
            bucket=influxdb_settings.influxdb_bucket,
            org=influxdb_settings.influxdb_org,
            record=record,
        )
        return True
    except Exception as e:
        logger.error(f"Error while writing to InfluxDB: {e}")
        return False
