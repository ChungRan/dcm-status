from .base import *

DEBUG = False

ALLOWED_HOSTS = ["localhost"]

CRONJOBS = [
    ('* 1 * * *', 'dcmStatus.cron.crawling_everyday', '>> /tmp/log/ggbc_cron.log'),
]
