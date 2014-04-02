from django.conf.urls import *
from .views import *


urlpatterns = patterns('',
       url(r'^(?P<module_id>[-\w]+)/$', get_flashcard, name='get_flashcard'),

    )