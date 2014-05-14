from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from course.models import Module


class Flashcard(models.Model):

    module = models.ForeignKey(Module, verbose_name=_("module"))
    summary = models.CharField(max_length=250, verbose_name=_("summary")) 
    description = models.CharField(max_length=2000, verbose_name=u'description')
    image = models.ImageField(upload_to = 'flashcards', blank=True)
    name = models.CharField(max_length=40, verbose_name=_("name")) 
    slug = models.SlugField(max_length=40)
    
    class Meta:
        verbose_name = _('Flashcard')
        verbose_name_plural = _('Flashcards')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Flashcard, self).save(*args, **kwargs)
    

class FlashcardCount(models.Model):
    flashcard = models.ForeignKey(Flashcard, verbose_name=_('flashcard'))
    user = models.ForeignKey(User, verbose_name=_('name'))
    access_type = models.CharField(max_length=20, verbose_name=_('acces type'))
    date = models.DateField(auto_now=True, verbose_name=_('date'))
    class Meta:
        verbose_name = _('FlashcardCount')
        verbose_name_plural = _('FlashcardCounts')

    def __unicode__(self):
        return self.flashcard

    