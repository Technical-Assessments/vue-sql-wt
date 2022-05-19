FROM python:3.10.4-slim-buster as basic

# Sys tools
RUN  apt-get update \
  && python -m pip install --upgrade pip \
  && apt-get install -y wget \
  && mkdir -m 777 -p ~/miniconda3 

WORKDIR /server

COPY --chmod=777 . .


ENTRYPOINT [ "./scripts/entrypoint.sh" ]