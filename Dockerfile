FROM python:3-alpine

LABEL org.opencontainers.image.source=https://github.com/andre4ik3/sleigh

WORKDIR /etc/sleigh
COPY . .

RUN apk add --no-cache alpine-sdk libffi-dev nginx
RUN pip install --no-cache-dir -U pip wheel pipenv
RUN pipenv install

EXPOSE 8443
CMD ["extra/start.sh"]
