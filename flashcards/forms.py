from pagedown.widgets import AdminPagedownWidget
from django import forms
from .models import Flashcard


class FlashcardModelForm(forms.ModelForm):
    description = forms.CharField(widget=AdminPagedownWidget())
    summary = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Flashcard
        fields = [ "name", "module", "summary", "description", "image"]


 