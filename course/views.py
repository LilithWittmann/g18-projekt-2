import datetime

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect, HttpResponse, HttpResponseBadRequest, HttpResponsePermanentRedirect
from django.template.response import TemplateResponse

from .models import Course, Module
from flashcards.models import *



@login_required
def courses_list(request):
    courses = Course.objects.all()
    return TemplateResponse(request, "courses_list.html", {"courses": courses})


@login_required
def modules_list(request, course_slug):
    try:
        course = Course.objects.filter(slug=course_slug).get()
    except ObjectDoesNotExist:
        raise Http404
    modules = Module.objects.filter(course=course.id).all()
    return TemplateResponse(request, "modules_list.html", {"course": course, "modules": modules})


@login_required
def module_show(request, course_slug, module_slug):
    try:
        course = Course.objects.filter(slug=course_slug).get()
    except ObjectDoesNotExist:
        raise Http404

    try:
        module = Module.objects.filter(slug=module_slug, course=course.id).get()
    except ObjectDoesNotExist:
        raise Http404

    flashcards = Flashcard.objects.filter(module=module.pk).all()

    flashcard_details = []
    for flashcard in flashcards:
        flashcard_details.append({
            "flashcard": flashcard,
            "stats": FlashcardCount.objects.filter(user=request.user, flashcard=flashcard).count()
        })


    return TemplateResponse(request, "module_show.html", {"module": module, "flashcards": flashcard_details})
