# Celery tasks
```
Package for handling tasks in async manner
```

## Usage of tasks
```python
from celery_tasks.tasks import scrape_countries


scrape_countries.apply_async(ignore_result=True)
```