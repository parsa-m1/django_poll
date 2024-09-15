from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify

from .models import *
def index(request):
    questions = Question.objects.all()

    return render(request, 'index.html', {'questions': questions})

def poll_detail(request, id):
    question = get_object_or_404(Question, id=id)

    if request.method == 'POST':
        voted = request.POST['voted']
        choice = get_object_or_404(Choice, id=int(voted))
        choice.vote += 1
        choice.save()


    return render(request, 'poll_detail.html', {'question': question})

def poll_results(request, q_id):
    pass


def poll_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    questions = Question.objects.filter(category=category)

    return render(request, 'index.html', {'questions': questions})
