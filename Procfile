web: uvicorn mywebsite_api.asgi:application --reload --host 0.0.0.0 --port $PORT
worker: ./manage.py rundramatiq --processes 1 --threads 1
