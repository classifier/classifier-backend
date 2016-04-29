from __future__ import absolute_import

from backend.celery import app

@app.task(ignore_result=True)
def predict(review):
    return 5  # The Spark task should be invoked from here
