FROM python:3.6-alpine
LABEL maintainer="u1234x1234@gmail.com"

RUN apk add --no-cache ffmpeg
RUN pip install youtube-dl schedule pyyaml

COPY sync.py /bin/sync.py

CMD ["python3", "/bin/sync.py"]
