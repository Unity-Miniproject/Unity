from django.contrib import admin
from .models import videoLink

# Register your models here.


class linkDisplay(admin.ModelAdmin):
    list_display = ('title', 'subject', 'link')
    list_display_links = ('title', 'subject', 'link')


admin.site.register(videoLink, linkDisplay)
