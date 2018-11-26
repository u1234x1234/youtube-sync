import logging
import os
import time
from subprocess import check_call

import schedule
import yaml

ROOT_DOWNLOAD_DIR = '/downloads/'


def download():
    try:
        with open('/to_sync.yml', 'r') as in_file:
            items = list(yaml.load_all(in_file))
        logging.info('Number of playlists: {}'.format(len(items)))

        for item in items[0]:
            path = item['path']
            url = item['playlist_url']

            download_dir = '{}/{}'.format(ROOT_DOWNLOAD_DIR, path)
            if not os.path.exists(download_dir):
                os.makedirs(download_dir)
                logging.info('Directory {} created.'.format(download_dir))

            args = ['youtube-dl', '-c',
                    '--socket-timeout', '10', '-i',
                    '--download-archive', '{}/downloaded.txt'.format(download_dir),
                    '--extract-audio', '--audio-format', 'mp3',
                    '-o', '{}/%(title)s.%(ext)s'.format(download_dir), url]
            check_call(args)

    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    schedule.every().day.do(download)

    while True:
        schedule.run_pending()
        time.sleep(1)
