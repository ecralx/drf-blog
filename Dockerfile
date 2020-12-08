FROM ubuntu:20.04

RUN apt-get update &&\
    apt-get install -y build-essential \
    python3 \
    python3-pip
RUN mkdir /app

COPY requirements.txt /

RUN pip3 install uwsgi && \
    pip3 install -r /requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 8000
CMD ["uwsgi", "--ini", "/app/uswgi.ini"]
