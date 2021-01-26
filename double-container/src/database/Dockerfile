FROM python:3.8.3-slim
RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt

EXPOSE 2021
CMD ["python", "/app/database.py"]
