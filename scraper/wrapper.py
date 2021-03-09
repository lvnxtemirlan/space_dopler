from typing import List

from core.schemas import Continents, Countries, Leagues
from scraper.nowgoal.scraper import Scraper
from scraper.nowgoal.utils import Utils


class Nowgoal:
    def __init__(self):
        self.scraper = Scraper()

    def get_continents(self) -> List[Continents]:
        continents = []
        raw_continents = [
            (1, "Intercontinental"),
            (2, "European"),
            (3, "America"),
            (4, "Asian"),
            (5, "Oceania"),
            (6, "Africa"),
        ]
        for continent in raw_continents:
            continents.append(Continents(id=continent[0], name=continent[1]))
        return continents

    def get_countries(self) -> List[Countries]:
        countries = []

        response = self.scraper.scrape_base_page()
        data = Utils.convert_regex_to_dict(data=response.text)
        for continent_id, data in data["data"].items():
            for country_id, i in enumerate(data):
                countries.append(
                    Countries(
                        continent_id=continent_id+1,
                        name=i[2]
                    )
                )

        return countries

    def get_leagues(self) -> List[Leagues]:
        leagues = []

        response = self.scraper.scrape_base_page()
        data = Utils.convert_regex_to_dict(data=response.text)
        for continent_id, data in data["data"].items():
            for country_id, i in enumerate(data):
                print(i)
                # leagues.append(
                #     Leagues(
                #         id=i[]
                #         continent_id=continent_id + 1,
                #         name=i[2]
                #     )
                # )

        return leagues