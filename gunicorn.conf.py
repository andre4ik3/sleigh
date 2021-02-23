import multiprocessing

wsgi_app = "main:app"
bind = "127.0.0.1:8080"
worker_class = "aiohttp.GunicornUVLoopWebWorker"
workers = multiprocessing.cpu_count() * 2 + 1
