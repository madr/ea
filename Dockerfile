FROM python:3 as deps
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG=0
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

FROM deps AS source

COPY ./src /app/

FROM source AS db

RUN mkdir -p /app/data
VOLUME /app/data
RUN ./manage.py migrate

FROM db AS finished

EXPOSE 13371/tcp
EXPOSE 13371/udp

CMD ./manage.py runserver 0.0.0.0:13371