.PHONY: collectstatic run test ci install install-dev migrations staticfiles

help:
	@echo "Available commands"
	@echo " - run              : runs the development server"
	@echo " - ci               : lints, checks migrations, runs tests and show coveragereport"
	@echo " - shellplus        : runs the development shell"
	@echo " - install          : installs production requirements"
	@echo " - install-dev      : installs development requirements"
	@echo " - setup-test-data  : erases the db and loads mock data"
	@echo " - isort            : sorts all imports of the project"
	@echo " - lint             : lints the codebase"

collectstatic:        
	docker-compose exec web python manage.py collectstatic --noinput

clean:
	docker-compose exec web rm -rf __pycache__ .pytest_cache
	rm -rf __pycache__ .pytest_cache

up:
	docker-compose up -d

down:
	docker-compose down

build:
	docker-compose down
	docker-compose up -d --build

logs:
	docker-compose logs -f web

shell_plus:
	docker-compose exec web python manage.py shell_plus

shell:
	docker-compose exec web python manage.py shell

dcps:
	docker-compose ps

showmigrations:
	docker-compose exec web python manage.py showmigrations

makemigrations:
	docker-compose exec web python manage.py makemigrations

migrate:
	docker-compose exec web python manage.py migrate

migrations-check:
	docker-compose exec web python manage.py makemigrations --check --dry-run

test: migrations-check
	docker-compose exec web python manage.py test -v 2

gittree:
	git log --graph --pretty=oneline --abbrev-commit

check:
	docker-compose exec web python manage.py check

check-deploy:
	docker-compose exec web python manage.py check --deploy

startjobs:
	docker-compose exec web python manage.py startjobs

ci: lint test

isort: 
	isort .

isort-check:
	isort -c .