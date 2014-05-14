from django.http import Http404, HttpResponseRedirect, HttpResponse, HttpResponseBadRequest, HttpResponsePermanentRedirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
import datetime

@login_required
def home(request):
    return HttpResponseRedirect(reverse("courses_list"))
