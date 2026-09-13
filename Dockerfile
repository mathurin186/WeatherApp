FROM python:3.15-rc-slim-bookworm

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "weather.py"]
