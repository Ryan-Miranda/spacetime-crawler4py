import os
from threading import Thread

from inspect import getsource
from utils.download import download
from utils import get_logger, clean_url
from utils.Tokenizer import Tokenizer
import scraper
import time


class Worker(Thread):
    def __init__(self, worker_id, config, frontier):
        self.logger = get_logger(f"Worker-{worker_id}", "Worker")
        self.config = config
        self.frontier = frontier
        self.tokenizer = Tokenizer()
        self.urls = set()
        # basic check for requests in scraper
        assert {getsource(scraper).find(req) for req in {"from requests import", "import requests"}} == {-1}, "Do not use requests from scraper.py"
        super().__init__(daemon=True)
        
    def run(self):
        while True:
            tbd_url = self.frontier.get_tbd_url()
            if tbd_url is not None:
                tmp_url = clean_url(tbd_url)
                self.save_to_unique_url_list(tmp_url)

            if not tbd_url:
                self.logger.info("Frontier is empty. Stopping Crawler.")
                 # TODO :: Print Result Data
                break
            resp = download(tbd_url, self.config, self.logger)
            self.logger.info(
                f"Downloaded {tbd_url}, status <{resp.status}>, "
                f"using cache {self.config.cache_server}.")
            scraped_urls = scraper.scraper(tbd_url, resp, self.tokenizer)
            for scraped_url in scraped_urls:
                self.frontier.add_url(scraped_url)
            self.frontier.mark_url_complete(tbd_url)
            time.sleep(self.config.time_delay)

    def save_to_unique_url_list(self, tmp_url):
        if tmp_url not in self.urls:
            self.urls.add(tmp_url)
            with open(os.getcwd() + '/' + 'tmp/unique_file_urls.txt', 'a') as uniq_url:
                uniq_url.write(tmp_url + '\n')
