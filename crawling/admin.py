from django.contrib import admin

# Register your models here.
from .models import Rank, CrawledDate, MinorGall, StatPostCount


admin.site.register(Rank)
admin.site.register(CrawledDate)
admin.site.register(MinorGall)
admin.site.register(StatPostCount)
