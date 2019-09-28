FROM alpine:latest

RUN apk add --update \
    python3 \
    python3-dev \
    libpq

RUN apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev

RUN pip3 install peewee
RUN pip3 install psycopg2
RUN pip3 install chalice

WORKDIR /app

COPY . /app

EXPOSE 8000

CMD ["chalice", "local", "--host", "0.0.0.0", "--port", "8000"]
