FROM python:3.9-slim-buster


WORKDIR /usr/src/app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install pipenv


COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --system --deploy


COPY . .

CMD ["python", "-W ignore", "app.py"]
