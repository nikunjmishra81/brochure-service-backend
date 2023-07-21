FROM python:3.8-slim-buster
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY ./ /app
RUN apt-get update
EXPOSE 8001

CMD ["python", "app.py"]
