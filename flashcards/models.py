from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings

from course.models import Module


class Flashcard(models.Model):

    module = models.ForeignKey(Module, verbose_name=_("module"))
    summary = models.CharField(max_length=250, verbose_name=_("summary")) 
    description = models.CharField(max_length=2000, verbose_name=u'description')
    image = models.ImageField(upload_to = 'flashcards')
    
    class Meta:
        verbose_name = _('Flashcard')
        verbose_name_plural = _('Flashcards')

    def __unicode__(self):
        return "%s - %s" % (self.module.name, self.pk)
    