import re


class Config(object):
    def __init__(self, config):
        self.user_agent = config["IDENTIFICATION"]["USERAGENT"].strip()
        print (self.user_agent)
        assert self.user_agent != "DEFAULT AGENT", "Set useragent in config.ini"
        assert re.match(r"^[a-zA-Z0-9_ ,]+$", self.user_agent), "User agent should not have any special characters outside '_', ',' and 'space'"
        self.threads_count = int(config["LOCAL PROPERTIES"]["THREADCOUNT"])
        self.save_file = config["LOCAL PROPERTIES"]["SAVE"]

        self.host = config["CONNECTION"]["HOST"]
        self.port = int(config["CONNECTION"]["PORT"])

        self.seed_urls = config["CRAWLER"]["SEEDURL"].split(",")
        self.time_delay = float(config["CRAWLER"]["POLITENESS"])

        self.cache_server = None
        self.request_time_out = int(config["REQUESTS"]["REQUEST_TIMEOUT"])

        # TMP
        self.tmp_folder=config['RESULTS']['URL_TMP']
        self.tmp_pages_folder=config['RESULTS']['URL_TMP_PAGES']
        self.tmp_pg_index_txt=config['RESULTS']['URL_PG_INDEX_TXT']
        self.unique_url_file = config['RESULTS']['URL_UNIQUE_FILE']

        # INFORMATION
        self.entropy_threshold = config['CRAWLER']['ENTROPY_THRESHOLD']
        self.similarity_threshold = config['CRAWLER']['SIMILARITY_THRESHOLD']
