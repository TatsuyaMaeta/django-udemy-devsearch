FROM python:3.8.13-slim-buster
WORKDIR /app
COPY ./app ./

RUN chmod +x /app/entrypoint.sh
CMD ["bash", "-c", "/app/entrypoint.sh"]

# RUN apt-get update
# RUN apt-get install -y vim less

# postgresqlのdev用のものをinstall
# RUN apt-get install -y libpq-dev 

# RUN pip install --upgrade pip --no-cache-dir

RUN pip install -r /app/requirements.txt  --no-cache-dir

# バイナリーのpostgresqlをrequirementsから切り分けてinstall
RUN pip install psycopg2-binary


# CMD [ "python3", "manage.py", "collectstatic" ]

CMD [ "python3","manage.py","runserver","0.0.0.0:8000"]


# CMD [ "gunicorn","main_app.wsgi:application","--bind","0.0.0.0:8000" ]