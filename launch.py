from configparser import ConfigParser
from argparse import ArgumentParser

from utils.server_registration import get_cache_server
from utils.config import Config
from crawler import Crawler
import os


def main(config_file, restart):
    create_local_tmp()
    cparser = ConfigParser()
    cparser.read(config_file)
    config = Config(cparser)
    config.cache_server = get_cache_server(config, restart)
    crawler = Crawler(config, restart)
    crawler.start()


def create_local_tmp():
    if not os.path.isdir('./tmp'):
        os.mkdir('./tmp')

    if not os.path.isdir('./tmp/pages'):
        os.mkdir('./tmp/pages')

    if not os.path.isdir('./tmp/cleanpages'):
        os.mkdir('./tmp/cleanpages')

    if not os.path.isfile('tmp/pg_index.txt'):
        with open('tmp/pg_index.txt', 'w') as f:
            f.write('# wordCount, hashVal, url, top50CommonWords' + '\n')

    if not os.path.isfile('./tmp/unique_file_urls.txt'):
        with open('tmp/unique_file_urls.txt', 'w') as f:
            f.write('#Unique URls' + '\n')


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--restart", action="store_true", default=False)
    parser.add_argument("--config_file", type=str, default="config.ini")
    args = parser.parse_args()
    main(args.config_file, args.restart)
