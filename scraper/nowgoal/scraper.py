import requests

from .utils import Utils


class Scraper:
    def __init__(self):
        self.host = Utils.read_json("scraper/nowgoal/resources/base.json")["host"]
        self.base_url = f"http://{self.host}/jsData/leftData/leftData.js"

    def scrape_base_page(self) -> requests.Response:

        """http://info.nowgoal3.com/jsData/leftData/leftData.js"""

        response: requests.Response = Utils().request_handle(url=self.base_url)

        return response
