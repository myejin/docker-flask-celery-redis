FROM python:3.7-slim-buster

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true

COPY . /api
WORKDIR /api 

RUN pip install -r requirements.txt
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
