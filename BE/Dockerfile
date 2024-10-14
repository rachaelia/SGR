# syntax=docker/dockerfile:1

FROM python:3.11.9
WORKDIR /BE
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader vader_lexicon
COPY . .
EXPOSE 8080
CMD ["waitress-serve","--call", "app:create_app"]