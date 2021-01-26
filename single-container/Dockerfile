FROM python:3.8.3-slim
RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt

EXPOSE 2020
CMD ["python", "/app/app.py"]
