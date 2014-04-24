from django.conf.urls import *
from .views import *


urlpatterns = patterns('',
       url(r'^$', courses_list, name='courses_list'),
       url(r'^(?P<course_slug>[-\w]+)/$', modules_list, name='modules_list'),
       url(r'^(?P<course_slug>[-\w]+)/(?P<module_slug>[-\w]+)$', module_show, name='module_show'),
)