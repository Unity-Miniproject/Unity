from students.views import subjects
from django.db.models.fields import CharField
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.db import models
from dynamic_models.models import ModelSchema, FieldSchema
from django.urls import clear_url_caches
from importlib import import_module, reload
from django.contrib import admin
from django.conf import settings
from .models import Modelnames
from django.utils.crypto import get_random_string
from subjects.models import Section, Semester, Branch, newClasses
import datetime
from django.utils.timezone import utc
# Create your views here.


def addModelEntries(request):
    return redirect('/admin')


def base(request):
    return render(request, 'base.html')



#creating class using dynamic models

def createClass(request):
    modelExists = False
    modelCreated = False
    classCode = get_random_string(8)
    classNotes = classCode + "notes"
    # classAssignment = classCode + "assignment"
    if request.POST:
        classCode = classCode
        className = request.POST['modelname']
        classBranch = request.POST['classbranch']
        classSemester = request.POST['classsemester']
        classSection = request.POST['classsection']
        try:
            #class model(database table)
            model_schema = ModelSchema.objects.create(
                name=classCode )
            #notes model
            model_schemanotes = ModelSchema.objects.create(
                name=classNotes)
            #assignemnt model
            # model_schemaassignment = ModelSchema.objects.create(
            #     name=classAssignment)
            modelCreated = True
        except Exception as e:
            modelExists = True
            createClass()
            context = {
                'modelExists': modelExists,
                'modelCreated': modelCreated, 
                'modelName': classCode,
                'branch' : Branch.objects.all(),
                'section': Section.objects.all(),
                'semester': Semester.objects.all(),
                }
            return render(request, 'dynamic_models/createModels.html',context)
        # field schema for class 
        field_schema = FieldSchema.objects.create(
            name='Topics',
            data_type='character',
            model_schema=model_schema,
            max_length=100,
            null=False,
            unique=False
        )
        field_schema = FieldSchema.objects.create(
            name='Video Link',
            data_type='url',
            model_schema=model_schema,
            null=True,
        )
        field_schema = FieldSchema.objects.create(
            name='Completed Date',
            data_type='date',
            model_schema=model_schema,
            null=True,
        )
        field_schema = FieldSchema.objects.create(
            name='Discription',
            data_type='richtext',
            model_schema=model_schema,
            null=True,
        )

        # field schema for notes model
        field_schema = FieldSchema.objects.create(
            name='question',
            data_type='richtext',
            model_schema=model_schemanotes,
            null=True,
        )
        field_schema = FieldSchema.objects.create(
            name='answer',
            data_type='richtext',
            model_schema=model_schemanotes,
            null=True,
        )


        # field schema for assignment model
        # field_schema = FieldSchema.objects.create(
        #     name='question',
        #     data_type='richtext',
        #     model_schema=model_schemaassignment,
        # )
        # field_schema = FieldSchema.objects.create(
        #     name='question',
        #     data_type='richtext',
        #     model_schema=model_schemaassignment,
        #     null=True,
        # )
        

        model_create = Modelnames.objects.create(
            modelname=classCode)
        model_create = Modelnames.objects.create(
            modelname=classNotes)
        # model_create = Modelnames.objects.create(
        #     modelname=classAssignment)
        reg_model = model_schema.as_model()
        reg_modelnotes = model_schemanotes.as_model()
        # reg_modelassignment = model_schemaassignment.as_model()
        admin.site.register(reg_model)
        admin.site.register(reg_modelnotes)
        # admin.site.register(reg_modelassignment)
        reload(import_module(settings.ROOT_URLCONF))
        #user created classes 
        newClasses.objects.create(classId=classCode,
                                  className=className, classSection=classSection, classBranch=classBranch, classSemester=classSemester, author=request.user, createdDate=datetime.datetime.utcnow().replace(tzinfo=utc))
        clear_url_caches()
        
    context={
        'modelExists': modelExists, 
        'modelCreated': modelCreated, 
        'modelName': classCode,
        'branch': Branch.objects.all(),
        'section': Section.objects.all(),
        'semester': Semester.objects.all(),
        }
    return render(request, 'dynamic_models/createModels.html',context)


def showObjectLists(request):
    modelNamesQuerySet = Modelnames.objects.all()
    modelNames = list()
    for model in modelNamesQuerySet:
        modelNames.append(model.modelname)
    cont_dict = {
        'modelNames': modelNames,
        'get': True
    }
    if request.POST:
        model = ModelSchema.objects.get(
            name=request.POST['modelname']).as_model()
        objList = model.objects.all().values()
        fieldNames = list()
        noEntry = False
        try:
            for x in objList[0]:
                fieldNames.append(x)
        except Exception as e:
            noEntry = True
        cont_dict = {
            'modelNames': modelNames,
            'objects': objList,
            'noEntry': noEntry,
            'fieldNames': fieldNames,
            'objectType': request.POST['modelname'],
            'get': False
        }
    return render(request, 'teachers/classdetails/index.html', context=cont_dict)



