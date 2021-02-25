#!/bin/sh
set -e
if [[ ! -e config/ssl/server.key ]]; then
  openssl req -x509 -nodes -newkey rsa:4096 \
    -keyout config/ssl/server.key \
    -out config/ssl/server.pem \
    -days 365
fi
nginx -s quit
nginx \
  -c $PWD/extra/nginx.conf \
  -e $PWD/extra/nginx-error.log
gunicorn main:app \
  --bind 127.0.0.1:8080 \
  --keep-alive 5 \
  --workers 6 \
  --worker-class aiohttp.GunicornUVLoopWebWorker \
  --max-requests 1000 \
  --max-requests-jitter 100
