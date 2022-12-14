FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./peaks /code/
RUN apt-get update -y \
    && apt-get -y install libpq-dev python3-dev postgresql-client \
    postgresql-server-dev-all

