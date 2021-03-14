from core.models import Continents, Countries, session
from scraper.wrapper import Nowgoal

nowgoal = Nowgoal()

data = nowgoal.get_leagues()
