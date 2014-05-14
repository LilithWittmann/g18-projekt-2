from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.template.response import TemplateResponse

from .forms import *
from .models import * 
from .utils import *

def show_question(request, module_slug):
    try:
        module = Module.objects.filter(slug=module_slug).get()
    except ObjectDoesNotExist:
        raise Http404

    if request.method == 'POST':
        question = Question.objects.filter(pk=request.POST.get("question_id"), module=module.pk).get()
        selected_answer = int(request.POST.get("answer"))
        for answer in question.get_answers():
            if answer.pk == selected_answer:
                if answer.is_correct:
                    print ("wright answer")
                    messages.success(request, "Right answer!")
                else:
                    print ("wrong answer")
                    messages.error(request, "Wrong answer!")
        
    question = Question.objects.filter(module=module).order_by('?')[0]
    
    return TemplateResponse(request, "question_show.html", {"question": question, "answers": QuestionForm(generate_answers(question), initial={"question_id": question.pk}), "module": module})


