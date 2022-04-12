from django.contrib import admin

from app.models import Access_Record, Topic, Webpage

# Register your models here.
admin.site.register(Topic)

admin.site.register(Webpage)

admin.site.register(Access_Record)


