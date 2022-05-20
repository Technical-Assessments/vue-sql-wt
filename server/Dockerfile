FROM python:3.10.4-slim-buster as basic

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /server

COPY --chmod=777 . .

RUN apt-get update \
  ; apt-get install --no-install-recommends -y gcc python3-dev g++ unixodbc-dev \
  ; pip install --no-cache-dir -r requirements/requirements.txt


CMD python manage.py runserver 0.0.0.0:${APP_PORT}