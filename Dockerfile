LABEL org.opencontainers.image.source=https://github.com/andre4ik3/sleigh
FROM python:3-alpine
RUN apk add --no-cache alpine-sdk libffi-dev nginx
WORKDIR /etc/sleigh
COPY . .
RUN pip install --no-cache-dir -U pip -r requirements.txt
EXPOSE 8443

ENTRYPOINT ["extra/start.sh"]
