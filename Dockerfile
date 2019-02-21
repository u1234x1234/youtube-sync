FROM python:3.6-alpine

LABEL maintainer="u1234x1234@gmail.com"
ENV USERNAME downloader
ENV OUTPUT_DIRECTORY /downloads

RUN apk add --no-cache ffmpeg
RUN pip install youtube-dl schedule pyyaml

COPY sync.py /bin/sync.py
RUN mkdir ${OUTPUT_DIRECTORY}

RUN adduser -D ${USERNAME} && \
    chown -R ${USERNAME}:${USERNAME} ${OUTPUT_DIRECTORY}

USER ${USERNAME}
CMD ["python3", "/bin/sync.py"]
