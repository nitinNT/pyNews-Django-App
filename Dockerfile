FROM python:3.6

ENV PYTHONBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000
STOPSIGNAL SIGINT

# - w workers to serve the more requests
CMD ["gunicorn", "-b",":8000","-w","3","newsapi.wsgi"]


