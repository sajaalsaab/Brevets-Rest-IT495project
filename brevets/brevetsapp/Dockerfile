FROM python:3.9
LABEL MAINTAINER "411201865@qu.edu.sa"

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT ["python"]
CMD ["flask_brevets.py"]