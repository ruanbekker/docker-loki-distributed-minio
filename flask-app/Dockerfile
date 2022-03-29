FROM python:3.8-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY boot.sh /src/boot.sh
RUN chmod +x /src/boot.sh
COPY requirements.txt /src/requirements.txt

RUN pip3 install -r /src/requirements.txt

ADD app.py /src/app.py

WORKDIR /src
ENTRYPOINT ["/src/boot.sh"]
