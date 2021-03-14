from dataclasses import dataclass
from typing import Optional


@dataclass
class Continents:
    id: int
    name: Optional[str]


@dataclass
class Countries:
    continent_id: int
    name: Optional[str]


@dataclass
class Leagues:
    id: int
    continent_id: int
    country_id: int
    name: Optional[str]
