# the version of the image we wanna store
FROM python:3.7-alpine
LABEL Damianstone el crack

# set env variables
ENV PYTHONUNBUFFERED 1

COPY ./requeriments.txt /requeriments.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requeriments.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# create the user who gonna run the app
RUN adduser -D user
USER user


