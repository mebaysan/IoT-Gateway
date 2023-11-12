# Introduction

This is an example app to simulate IoT Gateway for writing sensor data into InfluxDB2. An explanation video for CI & CD, Caprover deployment on my YouTube channel, BaysanSoft.

# ENV Variables

You can check [`settings.py`](src/settings.py) file to see all env variables. If you provide them in OS Env, they will be overriden.

Also, you can check [`.env.dev`](src/settings.py) file.


# Development

```bash
make start-devenv # up dev envs, apps

make stop-devenv # down dev envs, apps

make prune-devenv # down and prune dev envs, apps

make test

make format

make lint
```

# API

Endpoint: `/iot/measure`

```json
{"iot_device": "device_name", "measurement": "temperature", "value": 25.7}
```
