FROM python:3.11.2-slim-buster

RUN mkdir /cloud_coupon

WORKDIR /cloud_coupon

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/cloud_coupon"

COPY . .

COPY ./scripts/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y postgresql-client

RUN pip install -r requirements.txt

EXPOSE 8800

ENTRYPOINT ["/entrypoint.sh"]
