FROM python:3.10-slim

WORKDIR /app

COPY Pipfile.lock Pipfile.lock
RUN pip install pipenv
RUN pipenv install

COPY . .

CMD python src/app.py
