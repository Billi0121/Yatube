FROM python:3.13-slim

RUN mkdir /app

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt --no-cache-dir

COPY yatube/ /app

WORKDIR /app

CMD [ "gunicorn", "yatube.wsgi:application" ,"--bind", "0:8000"]