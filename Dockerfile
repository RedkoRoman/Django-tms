FROM python:3.11

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /code

#
RUN pip3 install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc
RUN apt-get update && apt-get install -y supervisor
RUN apt-get install -y netcat-traditional

#COPY requirements.txt .
COPY Pipfile .
COPY Pipfile.lock .

#RUN pip3 install -r requirements.txt
RUN pipenv install --system --deploy --ignore-pipfile

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

COPY . .

CMD ["sh", "entrypoint.sh"]