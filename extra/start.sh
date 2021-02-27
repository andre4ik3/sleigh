#!/bin/sh
set -e
if [[ ! -e config/ssl/server.key ]]; then
  openssl req -x509 -nodes -newkey rsa:4096 \
    -subj "/C=RU/ST=Moscow Oblast/L=Moscow/O=andre4ik3/CN=localhost" \
    -keyout config/ssl/server.key \
    -out config/ssl/server.pem \
    -days 365
fi
if [[ -e /run/nginx/nginx.pid ]]; then
  nginx -s quit
elif [[ ! -d /run/nginx ]]; then
  mkdir /run/nginx
fi
nginx -c $PWD/extra/nginx.conf
gunicorn main:app \
  --bind 127.0.0.1:8080 \
  --keep-alive 5 \
  --workers 6 \
  --worker-class aiohttp.GunicornUVLoopWebWorker \
  --max-requests 1000 \
  --max-requests-jitter 100
