from django.conf.urls import *
from .views import *


urlpatterns = patterns('',
       url(r'^$', courses_list, name='courses_list'),
       url(r'^(?P<course_name>[-\w]+)/$', modules_list, name='modules_list'),
)