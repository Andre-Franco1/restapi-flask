APP = restapi

test:
	@flake8 . --exclude .venv
	@pytest -v --disable-warnings

compose:
	@docker compose build
	@docker compose up

heroku:
	@heroku container:login
	@heroku container:push -a flask-rest-api web
	@heroku container:release -a flask-rest-api web