FROM tiangolo/uwsgi-nginx-flask:flask
RUN pip install psycopg2
COPY ./app /app
