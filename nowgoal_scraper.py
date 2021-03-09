from scraper.wrapper import Nowgoal
from core.models import Continents, Countries, session

nowgoal = Nowgoal()

data = nowgoal.get_leagues()
