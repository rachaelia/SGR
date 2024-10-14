# syntax=docker/dockerfile:1

FROM python:3.11.9
WORKDIR /BE
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python -m nltk.downloader punkt
COPY . .
EXPOSE 5000
CMD ["python","app.py"]