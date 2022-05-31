import asyncio
import logging
import os
from time import time

import aiohttp

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def read_text_file(directory, file):
    """
    Async version of the download_link method we've been using in the other examples.
    :param session: aiohttp ClientSession
    :param directory: directory to save downloads
    :param link: the url of the link to download
    :return:
    """

    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{directory}/{file}"

        # call read text file function
        read_text_content(file_path)
        logger.info('Downloaded %s', file)


def read_text_content(file_path):
    with open(file_path, 'r') as f:
        for index, line in enumerate(f):
            print("Line {}: {}".format(index, line.strip().replace("COLUMNS","SUCCESS")))


# Main is now a coroutine
def main():
    download_dir = "C:/Suganya/test"
    os.chdir(download_dir)
    for file in os.listdir():
        read_text_file(download_dir, file)


if __name__ == '__main__':
    ts = time()
    main()
    logger.info('Took %s seconds to complete', time() - ts)
