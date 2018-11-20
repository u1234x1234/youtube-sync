import schedule
import time
import json
import os
from subprocess import check_call

DOWNLOAD_DIR = '/downloads/'


def download():

    for path, url in items:
        out_dir = '{}/{}'.format(DOWNLOAD_DIR, path)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        args = ['youtube-dl', '-c',
                '--socket-timeout', '10', '-i',
                '--download-archive', 'downloaded.txt',
                '--extract-audio', '--audio-format', 'mp3',
                '-o', '{}/"%(title)s.%(ext)s"'.format(out_dir), url]
        check_call(args)


schedule.every(5).seconds.do(download)

while True:
    schedule.run_pending()
    time.sleep(1) 
