from django.http import Http404, HttpResponseRedirect, HttpResponse, HttpResponseBadRequest, HttpResponsePermanentRedirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Module
import datetime
from django.core.exceptions import ObjectDoesNotExist



@login_required
def courses_list(request):
    courses = Course.objects.all()
    return TemplateResponse(request, "courses_list.html", {"courses": courses})


@login_required
def modules_list(request, course_name):
    try:
        course = Course.objects.filter(slug=course_name).get()
    except ObjectDoesNotExist:
        raise Http404        
    modules = Module.objects.filter(course=course.id).all()
    return TemplateResponse(request, "modules_list.html", {"course": course, "modules": modules})

@login_required
def module_show(request, module_slug):
    raise Http404

