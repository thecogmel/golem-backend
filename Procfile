web: gunicorn golem.wsgi
release: src/manage.py makemigrations --noinput
release: src/manage.py collectstatic --noinput
release: src/manage.py migrate --noinput