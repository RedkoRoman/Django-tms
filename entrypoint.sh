until nc -z -v -w30 db 5432
do
  echo 'Waiting for database connection'
  sleep 5
done

#python manage.py runserver 0.0.0.0:8000

python manage.py collectstatic --noinput
#gunicorn blog.wsgi:application -c gunicorn_conf.py

supervisord -c /code/supervisord.conf

tail -f /dev/null