import os
import requests
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ranker.settings')

app = Celery('ranker')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task
def ive_korea_internal_api():
    url = "http://13.125.164.253/cron/update/following"
    requests.post(url)


@app.task
def following_one_crawl():
    url = "http://13.125.164.253/v2/follow/list"
    res = requests.get(url).json()
    url = "http://13.125.164.253/cron/new/downloads"
    for obj in res["items"]:
        market_appid = obj["market_appid"]
        if obj["market"] == "one":
            print(market_appid)
            requests.post(url, data={"market_appid": market_appid})


@app.task
def crawl_app_store_hourly():
    url = "http://13.125.164.253/cron/new/ranking"
    requests.post(url, data={"market": "all"})
    url = "http://13.125.164.253/cron/new/ranking/high"
    requests.post(url)


@app.task
def crawl_app_store_daily():
    url = "http://13.125.164.253/cron/new/ranking"
    requests.post(url, data={"market": "one"})


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute=0, tz='Asia/Seoul'),
        crawl_app_store_hourly(),
    )

    sender.add_periodic_task(
        crontab(minute=10, hour=0, tz='Asia/Seoul'),
        crawl_app_store_daily(),
    )

    sender.add_periodic_task(
        1200.0,
        ive_korea_internal_api(),
    )

    sender.add_periodic_task(
        crontab(minute=10, hour=12, tz='Asia/Seoul'),
        following_one_crawl(),
    )