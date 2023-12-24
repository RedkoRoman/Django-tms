FROM python:3.11

WORKDIR /code

RUN pip3 install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc
RUN apt-get install -y netcat-traditional

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system --deploy --ignore-pipfile

COPY entrypoint-test.sh .
RUN chmod +x entrypoint-test.sh

COPY . .

CMD ["sh", "entrypoint-test.sh"]