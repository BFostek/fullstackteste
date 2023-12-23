FROM python:3.8

LABEL authors="brenomartins"

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "./main.py"]