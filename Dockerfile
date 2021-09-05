#./Dockerfile 
FROM ubuntu:18.04

ENV PYTHONUNBUFFERED=0

RUN apt-get update && \
    apt-get install -y python3-pip python3-dev && \
    apt-get clean

WORKDIR /web/

ADD ./requirements.txt /web/
RUN pip3 install -r requirements.txt

ADD . /web/

EXPOSE 80

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "dcmStatus.wsgi"]