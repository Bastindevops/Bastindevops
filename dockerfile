FROM python:3.11-slim

WORKDIR /usr/src/app

COPY app.py requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
