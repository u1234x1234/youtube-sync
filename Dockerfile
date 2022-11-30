FROM python:3.7-alpine

LABEL maintainer="u1234x1234@gmail.com"
ENV USERNAME youtube_sync
ENV OUTPUT_DIRECTORY /downloads

COPY requirements.txt /tmp/requirements.txt
RUN apk add --no-cache ffmpeg gcc musl-dev && \
    pip install -r /tmp/requirements.txt && \
    apk del gcc musl-dev && \
    rm -rf /var/cache/apk/*

COPY youtube_sync.py /bin/youtube_sync.py
RUN mkdir ${OUTPUT_DIRECTORY}

RUN adduser -D ${USERNAME} && \
    chown -R ${USERNAME}:${USERNAME} ${OUTPUT_DIRECTORY}

USER ${USERNAME}
CMD ["python", "/bin/youtube_sync.py"]
