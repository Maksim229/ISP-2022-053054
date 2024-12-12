FROM python:3.9-slim-bullseye
WORKDIR /ferst
COPY . .
CMD ["python", "main.py"]
