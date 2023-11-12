#! /bin/bash

gunicorn main:app --bind 0.0.0.0:8080 -w 4 -k uvicorn.workers.UvicornWorker

# uvicorn main:app --host 0.0.0.0 --port 8080 --proxy-headers --workers 4