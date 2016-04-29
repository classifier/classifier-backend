from __future__ import absolute_import

from celery import Celery

app = Celery('backend',
             broker='redis://127.0.0.1:6379',
             backend='redis://127.0.0.1:6379',
             include=['backend.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=1000,
)

if __name__ == '__main__':
    app.start()
