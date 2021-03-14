from celery import Celery

from core.models import Country
from scraper.wrapper import Nowgoal

nowgoal = Nowgoal()
app = Celery("celery_tasks", broker="redis://localhost", backend="redis://localhost")


@app.task
def scrape_countries():
    countries = nowgoal.get_countries()

    for country in countries:
        _country = Country.create(continent_id=country.continent_id, name=country.name)

    return "success"
