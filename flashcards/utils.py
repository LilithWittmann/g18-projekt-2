from .models import FlashcardCount

def count_flashcard_access(user, flashcard, access_type="tour"):
	counter = FlashcardCount()
	counter.user = user 
	counter.flashcard = flashcard
	counter.access_type  = access_type
	counter.save()
	return FlashcardCount.objects.filter(user=user, flashcard=flashcard).count()