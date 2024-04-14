# syntax=docker/dockerfile:1

FROM python:3.10.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt 

COPY . .

ENV PYTHONUNBUFFERED=1

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
