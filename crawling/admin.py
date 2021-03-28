from django.contrib import admin

# Register your models here.
from .models import Rank, CrawledDate


admin.site.register(Rank)
admin.site.register(CrawledDate)
