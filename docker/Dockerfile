FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ../src/ .

RUN pip install --upgrade pip  

RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN mkdir -p /var/log/myapp/myappgw.log

RUN chmod 777 /var/log/myapp/myappgw.log

RUN touch /var/log/myapp/myappgw.log

RUN chmod 777 /var/log/myapp/myappgw.log

EXPOSE 8080

# HEALTHCHECK --interval=1m --timeout=30s --start-period=1m --retries=5 \
#     CMD curl -s http://localhost:8080/health || exit 1

ENTRYPOINT [ "bash", "entrypoint.sh" ]