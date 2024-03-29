FROM python:3.9-buster

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

EXPOSE 8000

COPY main.py /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]