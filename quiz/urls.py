from django.conf.urls import *
from .views import *


urlpatterns = patterns('',
       url(r'^(?P<module_slug>[-\w]+)/$', show_question, name='show_question'),

    )