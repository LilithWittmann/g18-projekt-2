from django.conf.urls import *
from .views import *


urlpatterns = patterns('',
       url(r'^(?P<module_slug>[-\w]+)/$', get_flashcard, name='get_flashcard'),
       url(r'^(?P<module_slug>[-\w]+)/(?P<flashcard_slug>[-\w]+)$', get_flashcard_permalink, name='get_flashcard_permalink'),

    )