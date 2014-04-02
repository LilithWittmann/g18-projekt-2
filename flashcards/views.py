from django.http import Http404, HttpResponseRedirect, HttpResponse, HttpResponseBadRequest, HttpResponsePermanentRedirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Flashcard
from course.models import Course, Module
import datetime

@login_required
def get_flashcard(request, module_id):
    module = Module.objects.filter(pk=module_id).get()
    if not module:
        raise Http404
    #TODO: Hack for prototyping, dont do this in production
    flashcard = Flashcard.objects.filter(module=module.id).order_by('?')[0]
    return TemplateResponse(request, "flashcard_show.html", {"flashcard": flashcard})



