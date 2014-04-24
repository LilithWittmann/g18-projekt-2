from django.http import Http404, HttpResponseRedirect, HttpResponse, HttpResponseBadRequest, HttpResponsePermanentRedirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .models import Flashcard
from course.models import Course, Module
import datetime

@login_required
def get_flashcard(request, module_slug):
    try:
        module = Module.objects.filter(slug=module_slug).get()
    except ObjectDoesNotExist:
        raise Http404

    #TODO: Hack for prototyping, dont do this in production
    flashcard = Flashcard.objects.filter(module=module.id).order_by('?')[0]
    return TemplateResponse(request, "flashcard_show.html", {"flashcard": flashcard, "module": module})



def get_flashcard_permalink(request, module_slug, flashcard_slug):
    try:
        module = Module.objects.filter(slug=module_slug).get()
    except ObjectDoesNotExist:
        raise Http404

    try:
        flashcard = Flashcard.objects.filter(module=module.id, slug=flashcard_slug).get()
    except ObjectDoesNotExist:
        raise Http404

    return TemplateResponse(request, "flashcard_show.html", {"flashcard": flashcard, "module": module})





