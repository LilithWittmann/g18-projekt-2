from django.db import models
from course.models import Module
from flashcards.models import Flashcard
from django.utils.translation import ugettext as _

class Question(models.Model):

    text = models.CharField(max_length=100)
    module = models.ForeignKey(Module)
    flashcard = models.ForeignKey(Flashcard)
    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')

    def __unicode__(self):
        return self.text

    def get_answers(self):
        return Answer.objects.filter(question=self.pk).all()


class Answer(models.Model):
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question)
    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')

    def __unicode__(self):
        return self.text
    

    