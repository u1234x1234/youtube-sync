import logging
import os
import time
from subprocess import check_output

import schedule
import yaml

ROOT_DOWNLOAD_DIR = os.environ['OUTPUT_DIRECTORY'] # defined in Dockefile


def download():
    try:
        with open('/config.yml', 'r') as in_file:
            items = list(yaml.load_all(in_file))
        logging.info('Number of playlists: {}'.format(len(items)))

        for item in items[0]:
            path = item['name']
            url = item['playlist_url']
            args = item.get('args', '')

            download_dir = os.path.join(ROOT_DOWNLOAD_DIR, path)
            if not os.path.exists(download_dir):
                os.makedirs(download_dir)
                logging.info('Directory {} created.'.format(download_dir))

            command = ['youtube-dl', '-c',
                       '--socket-timeout', '10', '-i',
                       '--download-archive', '{}/downloaded.txt'.format(download_dir)] + \
                       args.split(' ') + \
                       ['-o', '{}/%(title)s.%(ext)s'.format(download_dir), url]
            try:
                command_output = check_output(command)
                logging.debug(command_output)
            except Exception as e:
                logging.exception(e)

    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    schedule.every().day.do(download)

    while True:
        schedule.run_pending()
        time.sleep(1)
