FROM python:3.12.3

WORKDIR /app

COPY /app /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD flask run --host=0.0.0.0 --port=3000