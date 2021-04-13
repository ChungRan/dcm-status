# dcm-status

DcMinorGall 순위 크롤링앱

## Stack

* Django
  * [django-crontab](https://github.com/kraiz/django-crontab)
  * [Tailwind css (django-tailwind)](https://github.com/timonweb/django-tailwind)

* Crawling
  * beautifulsoup4

* Deploy
  * Heroku
  * GCP

## Script
### django-tailwind
`python manage.py tailwind start`   

`python manage.py tailwind build`

### django-crontab
`python manage.py crontab add`

`python manage.py crontab show`

`python manage.py crontab remove`

### MinorGall Crawling
`python manage.py minor_crawling`