from django.contrib import admin
from .models import StudentDetails

# Register your models here.

admin.site.site_header = 'Bmsit & M'


class StudentDisplay(admin.ModelAdmin):
    list_display = ('usn', 'name', 'email', 'branch', 'semester', 'section')
    list_display_links = ['usn', 'name',
                          'email', 'branch', 'semester', 'section']


admin.site.register(StudentDetails, StudentDisplay)
