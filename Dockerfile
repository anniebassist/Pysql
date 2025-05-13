FROM python:3.12-slim
WORKDIR /usr/src/apps
COPY requirements.txt ./
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
RUN pip install --no-cache-dir  -r requirements.txt
COPY . .
EXPOSE 80
CMD ["uvicorn","app:app","--host","0.0.0.0","--port","80"]





