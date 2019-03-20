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
            items = list(yaml.load_all(in_file))[0]
        logging.info('Number of playlists: {}'.format(len(items)))

        for item in items:
            path = item['name']
            url = item['playlist_url']
            args = item.get('args', None)

            download_dir = os.path.join(ROOT_DOWNLOAD_DIR, path)
            if not os.path.exists(download_dir):
                os.makedirs(download_dir)
                logging.info('Directory {} created.'.format(download_dir))

            command = ['youtube-dl', '--continue', '--ignore-errors',
                       '--socket-timeout', '10',
                       '--download-archive', '{}/downloaded.txt'.format(download_dir),
                       '-o', '{}/%(title)s.%(ext)s'.format(download_dir), url]
            if args:
                command += args.split(' ')
            logging.debug('Command to execute: [{}]'.format(command))
            try:
                command_output = check_output(command)
                logging.debug(command_output)
            except Exception as e:
                logging.exception(e)

    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s.%(funcName)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )
    schedule.every().day.do(download)
    download()

    while True:
        schedule.run_pending()
        time.sleep(1)
