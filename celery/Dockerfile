FROM python:3.7-slim-buster

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true

COPY . /celery
WORKDIR /celery 

RUN pip install -r requirements.txt 
ENTRYPOINT celery -A tasks worker --loglevel=info --autoscale=3,1