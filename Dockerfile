from arm64v8/python:3.12-alpine

LABEL org.opencontainers.image.authors="minkhantzaw.personal@gmail.com"

COPY . /app/

WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV HOST=0.0.0.0

ENV PORT=8080

CMD ["python3", "main.py"]
