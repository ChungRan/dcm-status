#./Dockerfile 
FROM python:3.9.4

RUN apt-get -y update

## Copy all src files 
WORKDIR /web
COPY . .

## Install packages 
RUN pip install -r requirements.txt

## Run the application on the port 8080 
EXPOSE 8000


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "dcmStatus.wsgi:application"]