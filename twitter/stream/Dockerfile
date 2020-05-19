FROM python:3.7.4-stretch
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python3","tweepy_streamer.py"]