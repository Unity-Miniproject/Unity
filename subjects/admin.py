from django.contrib import admin
from .models import WtLab, AcA, ML, SaN, CC, MlLab, WT, project


# Register your models here.

class TopicDisplay(admin.ModelAdmin):
    list_display = ('section', 'topic')
    list_display_links = ['section', 'topic']


admin.site.register(WT, TopicDisplay)
admin.site.register(AcA, TopicDisplay)
admin.site.register(ML, TopicDisplay)
admin.site.register(SaN, TopicDisplay)
admin.site.register(CC, TopicDisplay)
admin.site.register(MlLab, TopicDisplay)
admin.site.register(WtLab, TopicDisplay)
admin.site.register(project, TopicDisplay)
