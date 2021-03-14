from celery import Celery

from scraper.wrapper import Nowgoal
from core.models import Country


app = Celery('tasks',
             broker="redis://localhost",
             backend="redis://localhost")
nowgoal = Nowgoal()


@app.task
def scrape_countries():
    countries = nowgoal.get_countries()

    for country in countries:
        _country = Country.fill()
