from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from django.shortcuts import render, redirect
from students.models import StudentDetails
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from subjects.models import newClasses
from subjects.models import Modelnames
from dynamic_models.models import ModelSchema, FieldSchema
import datetime
from django.urls import clear_url_caches
from django.utils.timezone import utc
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
from io import BytesIO
from django.views import View

@login_required
class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def teacherlogin(self):
        if login_required():
            return redirect('teacherprofile')
        else:
            return redirect('googlelogin')


@login_required
def teachers(request):
    return redirect('teacherprofile')


@login_required
def teacherProfile(request):

    context = {
        'classes' : newClasses.objects.filter(author=request.user)
    }
    return render(request, 'teachers/profile/index.html', context)


@login_required
def studentsList(request):
    context = {
        'students': StudentDetails.objects.all()
    }
    return render(request, 'teachers/studentsdetails/index.html', context)


@login_required
def createClass(request, slug):
    context = {

    }
    return render(request, 'teachers/createclass/index.html')


def viewClass(request, slug):
    if request.POST:
        classtopic = request.POST.get('syllabustopic')
        video_link = request.POST.get('videolink')
        topic_desc = request.POST.get('topicdescription')
        date_time = datetime.datetime.utcnow()
        topicupdate = ModelSchema.objects.get(name=slug).as_model()
        topicupdate.objects.create(
            topics=classtopic,
            video_link=video_link,
            completed_date=date_time,
            discription=topic_desc
        )
        clear_url_caches()
    model = ModelSchema.objects.get(name=slug).as_model()
    objList = model.objects.all().values()
    fieldNames = list()
    noEntry = False
    try:
        for x in objList[0]:
            fieldNames.append(x)
    except Exception as e:
        noEntry = True
    cont_dict = {
        'objects': objList,
        'noEntry': noEntry,
        'fieldNames': fieldNames,
        'objectType': slug,
        'classnotes' : slug+"notes"
    }
    return render(request, 'teachers/classdetails/index.html', context=cont_dict)


def classNotes(request, slug):
    if request.POST:
        question = request.POST['classnotesquestion']
        answer = request.POST['classnotesanswer']
        qaupdate = ModelSchema.objects.get(name=slug).as_model()
        qaupdate.objects.create(
            question=question,
            answer=answer
        )
        clear_url_caches()
    model = ModelSchema.objects.get(name=slug).as_model()
    objList = model.objects.all().values()
    fieldNames = list()
    noEntry = False
    try:
        for x in objList[0]:
            fieldNames.append(x)
    except Exception as e:
        noEntry = True
    context={
        'objects': objList,
        'noEntry': noEntry,
        'fieldNames': fieldNames,
        'objectType': slug,
        'classnotes': slug+"notes"
    }
    return render(request, 'teachers/notes/index.html', context)


def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


#Opens up page as PDF


def ViewPDF(request, slug):
    model = ModelSchema.objects.get(name=slug).as_model()
    objList = model.objects.all().values()
    fieldNames = list()
    noEntry = False
    try:
        for x in objList[0]:
            fieldNames.append(x)
    except Exception as e:
        noEntry = True
    context = {
        'objects': objList,
        'noEntry': noEntry,
        'fieldNames': fieldNames,
        'objectType': slug,
    }
    pdf = render_to_pdf('notes/pdf_template.html', context)
    return HttpResponse(pdf, content_type='application/pdf')

#Automaticly downloads to PDF file
def DownloadPDF(request,slug):
    model = ModelSchema.objects.get(name=slug).as_model()
    print(model)
    objList = model.objects.all().values()
    fieldNames = list()
    noEntry = False
    try:
        for x in objList[0]:
            fieldNames.append(x)
    except Exception as e:
        noEntry = True
    context = {
        'objects': objList,
        'noEntry': noEntry,
        'fieldNames': fieldNames,
        'objectType': slug,
    }

    pdf = render_to_pdf('notes/pdf_template.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = "notes.pdf"
    content = "attachment; filename='%s'" % (filename)
    response['Content-Disposition'] = content
    return response
