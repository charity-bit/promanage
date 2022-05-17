serve:
	python3 manage.py server

init:
	python3 manage.py db init

migrate:
	python3 manage.py db migrate -m "migration"

upgrade:
	python3 manage.py db upgrade

shell:
	python3 manage.py shell


