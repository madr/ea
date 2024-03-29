FROM python:3 as deps
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

FROM deps AS source

COPY ./src /app/

FROM source AS db

RUN mkdir -p /app/data
VOLUME /app/data
RUN ./manage.py collectstatic --noinput

FROM db AS finished

ENV SECRET_KEY="stockholmsblodbad1520varenbluff-nejdetvardetinte-sjundetillniondenovember1520"

EXPOSE 13371/tcp
EXPOSE 13371/udp

CMD waitress-serve --port=13371 ea:wsgi.application