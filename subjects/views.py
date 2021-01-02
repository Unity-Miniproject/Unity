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
# Create your views here.


def addModelEntries(request):
    return redirect('/admin')


def base(request):
    return render(request, 'base.html')


def createModels(request):
    modelExists = False
    modelCreated = False
    modelName = ''
    if request.POST:
        modelName = request.POST['modelname']
        try:
            model_schema = ModelSchema.objects.create(
                name=request.POST['modelname'])
            modelCreated = True
        except Exception as e:
            modelExists = True
            return render(request, 'dynamic_models/createModels.html', context={'modelExists': modelExists, 'modelCreated': modelCreated, 'modelName': modelName})
        len_req = (len(request.POST) - 2) // 5
        count = 0
        for x in range(len_req):
            count = count + 1
            field_schema = FieldSchema.objects.create(
                name=request.POST['field' + str(count)],
                data_type=request.POST['datatype' + str(count)],
                model_schema=model_schema,
                max_length=request.POST['maxlen' + str(count)],
                null=request.POST['null' + str(count)],
                unique=request.POST['unique' + str(count)]
            )
        model_create = Modelnames.objects.create(
            modelname=request.POST['modelname'])
        reg_model = model_schema.as_model()
        admin.site.register(reg_model)
        reload(import_module(settings.ROOT_URLCONF))
        clear_url_caches()
    return render(request, 'dynamic_models/createModels.html', context={'modelExists': modelExists, 'modelCreated': modelCreated, 'modelName': modelName})

#creating class using dynamic models

def createClass(request):
    modelExists = False
    modelCreated = False
    classCode = get_random_string(8)
    if request.POST:
        # className = request.POST['modelname']
        try:
            model_schema = ModelSchema.objects.create(
                name=classCode )
            modelCreated = True
        except Exception as e:
            modelExists = True
            createClass()
            return render(request, 'dynamic_models/createModels.html', context={'modelExists': modelExists, 'modelCreated': modelCreated, 'modelName': classCode})
        field_schema = FieldSchema.objects.create(
            name='Subject',
            data_type='character',
            model_schema=model_schema,
            max_length=100,
            null=False,
            unique=False
        )
        field_schema = FieldSchema.objects.create(
            name='Branch',
            data_type='character',
            model_schema=model_schema,
            max_length=20,
            null=False,
            unique=False
        )
        field_schema = FieldSchema.objects.create(
            name='Semester',
            data_type='character',
            model_schema=model_schema,
            max_length=20,
            null=False,
            unique=False
        )
        field_schema = FieldSchema.objects.create(
            name='Section',
            data_type='character',
            model_schema=model_schema,
            max_length=20,
            null=False,
            unique=False
        )
        model_create = Modelnames.objects.create(
            modelname=classCode)
        reg_model = model_schema.as_model()
        admin.site.register(reg_model)
        reload(import_module(settings.ROOT_URLCONF))
        clear_url_caches()
    return render(request, 'dynamic_models/createModels.html', context={'modelExists': modelExists, 'modelCreated': modelCreated, 'modelName': classCode})


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
    return render(request, 'displayObjects.html', context=cont_dict)
