from django.contrib import admin
from dynamic_models.models import ModelSchema
from .models import Modelnames, Section, Semester, Branch, newClasses

# Register your models here.
models = Modelnames.objects.all()
for model in models:
    reg_model = ModelSchema.objects.get(name=model.modelname).as_model()
    admin.site.register(reg_model)


class detailDisplay(admin.ModelAdmin):
    list_display = ('name', 'fullname')
    list_display_links = ['name', 'fullname']


admin.site.register(Branch, detailDisplay)
admin.site.register(Semester, detailDisplay)
admin.site.register(Section, detailDisplay)
admin.site.register(newClasses)
