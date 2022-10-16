FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG=0
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY ./src /app/
RUN mkdir /app/data
RUN ./manage.py migrate

EXPOSE 13371/tcp
EXPOSE 13371/udp

VOLUME /app/data

CMD ./manage.py runserver 0.0.0.0:13371