web: python src/manage.py runserver

release: python src/manage.py makemigrations --noinput
release: python src/manage.py collectstatic --noinput
release: python src/manage.py migrate --noinput