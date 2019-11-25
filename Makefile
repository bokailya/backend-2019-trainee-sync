up:
	docker-compose pull
	docker-compose up --build -d

down:
	docker-compose down

lint:
	pip install -r requirements/dev-requirements.txt
	flake8 src
	PYTHONPATH=src/ pylint src
	mypy src

format:
	pip install -r requirements/dev-requirements.txt
	black --verbose --config black.toml src
	isort --recursive src --skip src/pitter/migrations

test:
	pip install -r requirements/dev-requirements.txt
	pytest -s -vv
