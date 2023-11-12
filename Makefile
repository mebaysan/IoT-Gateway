install:
	@pip install -r src/requirements.txt

run:
	@python src/main.py

run_gunicorn:
	@gunicorn src.main:app --bind 0.0.0.0:8000 -w 4 -k uvicorn.workers.UvicornWorker

format:
	@black src

lint:
	@flake8 src

test:
	@pytest src/ -vv --disable-warnings --cov

coverage:
	@coverage report -m
	@coverage html
	@coverage xml

start-devenv:
	@docker compose -f ./docker/docker-compose.dev.yml up -d --build 

stop-devenv:
	@docker compose -f ./docker/docker-compose.dev.yml down
	
prune-devenv:
	@docker compose -f ./docker/docker-compose.dev.yml down -v