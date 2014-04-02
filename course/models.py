from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify

class Course(models.Model):

    name = models.CharField(max_length=40, verbose_name=_("name"))
    slug = models.SlugField(max_length=40)


    class Meta:
        verbose_name = _('course')
        verbose_name_plural = _('courses')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(test, self).save(*args, **kwargs)

class Module(models.Model):

    name = models.CharField(max_length=40, verbose_name=_("name"))
    description = models.CharField(max_length=400, verbose_name=_("description"))
    course = models.ForeignKey(Course, verbose_name=_("course"))


    class Meta:
        verbose_name = _('module')
        verbose_name_plural = _('modules')

    def __unicode__(self):
        return self.name

    