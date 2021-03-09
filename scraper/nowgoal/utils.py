import ast
import json
import re
from typing import Dict

import dataclass_factory
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class Utils:
    def __init__(self):
        self.headers = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/84.0.4147.135 Mobile Safari/537.36",
        }

    def requests_retry_session(
        self,
        retries=3,
        backoff_factor=0.3,
        status_forcelist=(500, 502, 504),
        session=None,
    ):
        session = session or requests.Session()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session

    def request_handle(self, url: str, **kwargs) -> requests.Response:
        headers = self.headers
        if "headers" in kwargs:
            headers = kwargs["headers"]
        with requests.Session() as session:
            session.headers.update(headers)
            response = self.requests_retry_session(session=session).get(url=url)
        return response

    @staticmethod
    def convert_regex_to_dict(data: str) -> Dict[str, dict]:
        end_data = {"data": {}}
        pre_data = re.findall(
            r"arrArea\[(?:(0|1|2|3|4|5)?)\] = (\[\[.*?\])\;",
            data,
        )
        for _str_list in pre_data:
            end_data["data"][int(_str_list[0])] = ast.literal_eval(_str_list[1])
        return end_data

    @staticmethod
    def read_json(filename: str) -> Dict:
        with open(filename, "r") as read_file:
            data = json.load(read_file)
        return data

    @staticmethod
    def load_schema(schema, args: dict) -> dict:
        factory = dataclass_factory.Factory()
        selection = factory.load(args, schema)
        serialized: dict = factory.dump(selection)

        return serialized
