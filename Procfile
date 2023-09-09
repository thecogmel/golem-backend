web: poetry shell
web: python src/manage.py runserver
web: gunicorn honeyhub-back.wsgi

release: python src/manage.py makemigrations --noinput
release: python src/manage.py collectstatic --noinput
release: python src/manage.py migrate --noinput