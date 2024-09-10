from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify

from .models import *
def index(request):
    questions = Question.objects.all()

    return render(request, 'index.html', {'questions': questions})

def poll_detail(request, slug):
    question = get_object_or_404(Question, slug=slug)

    return render(request, 'poll_detail.html', {'question': question})
def poll_results(request, slug):
    pass
