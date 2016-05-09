from __future__ import absolute_import

from backend.celery import app
from django.http import JsonResponse
import random

@app.task(ignore_result=True)
def predict(review):
    return JsonResponse({"result": random.randint(1,5)})
