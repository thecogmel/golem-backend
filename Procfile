web: python manage.py runserver
web: gunicorn honeyhub-back.wsgi

release: python manage.py makemigrations --noinput
release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput