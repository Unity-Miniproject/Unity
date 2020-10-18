from django.contrib import admin
from .models import Bmsit_Students

# Register your models here.

admin.site.site_header = 'Bmsit & M'


class StudentDisplay(admin.ModelAdmin):
    list_display = ('usn', 'name', 'email', 'branch', 'semester')
    list_display_links = ['usn', 'name', 'email', 'branch', 'semester']


admin.site.register(Bmsit_Students, StudentDisplay)
