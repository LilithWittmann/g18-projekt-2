from django.contrib import admin
from .models import Flashcard
from .forms import FlashcardModelForm


class FlashcardModelAdmin(admin.ModelAdmin):
    form = FlashcardModelForm

admin.site.register(Flashcard, FlashcardModelAdmin)
