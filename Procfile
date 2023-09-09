release: python src/manage.py makemigrations --noinput
release: python src/manage.py collectstatic --noinput
release: python src/manage.py migrate --noinput

web: python src/manage.py runserver 0.0.0.0:$PORT
web: gunicorn golem.wsgi

