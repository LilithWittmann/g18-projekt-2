from django import forms

class QuestionForm(forms.Form):
    answer = forms.ChoiceField(widget=forms.RadioSelect())
    question_id = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, answers, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['answer'].choices = answers