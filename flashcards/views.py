from django.http import Http404, HttpResponseRedirect, HttpResponse, HttpResponseBadRequest, HttpResponsePermanentRedirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .models import Flashcard
from .utils import *
from course.models import Course, Module
import datetime


@login_required
def get_flashcard(request, module_slug):
    try:
        module = Module.objects.filter(slug=module_slug).get()
    except ObjectDoesNotExist:
        raise Http404
    previous_card = request.GET.get('previous')

    #TODO: Hack for prototyping, dont do this in production
    flashcard = Flashcard.objects.filter(module=module.id).order_by('?')[0]
    card_views = count_flashcard_access(request.user, flashcard)
    return TemplateResponse(request, "flashcard_show.html", {"flashcard": flashcard, "module": module, "card_views": card_views, "previous_card": previous_card, "in_tour": True})



def get_flashcard_permalink(request, module_slug, flashcard_slug):
    try:
        module = Module.objects.filter(slug=module_slug).get()
    except ObjectDoesNotExist:
        raise Http404

    try:
        flashcard = Flashcard.objects.filter(module=module.id, slug=flashcard_slug).get()
    except ObjectDoesNotExist:
        raise Http404
    card_views = count_flashcard_access(request.user, flashcard, "direct_access")
    return TemplateResponse(request, "flashcard_show.html", {"flashcard": flashcard, "module": module, "card_views": card_views})





