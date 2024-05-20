FROM python:3.10

WORKDIR /app

COPY models /app/models
COPY routes /app/routes
COPY config /app/config 
COPY requirements.txt /app
COPY app.py /app

ENV PYTHONPATH=/app
ENV POSTGRES_DB=gestaopedidos
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=3EFNQnnKL8He
ENV POSTGRES_HOST=database-1.ctiiec6qy7gg.us-east-2.rds.amazonaws.com
ENV POSTGRES_PORT=5432

RUN python3 -m pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 5000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000", "--no-server-header", "--no-access-log"]