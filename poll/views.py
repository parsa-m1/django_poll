from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .models import *
def index(request):
    questions = Question.objects.all()

    return render(request, 'index.html', {'questions': questions})

def poll_detail(request, id):
    question = get_object_or_404(Question, id=id)

    if request.method == 'POST':
        question.participants.add(request.user)
        voted = request.POST['voted']
        choice = get_object_or_404(Choice, id=int(voted))
        choice.vote += 1
        choice.save()

    context = {'question': question,
        'is_voted': question.is_voted(request.user),
    }
    return render(request, 'poll_detail.html', context)

def poll_results(request, q_id):
    pass


def poll_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    questions = Question.objects.filter(category=category)

    return render(request, 'index.html', {'questions': questions})


def signup_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
        print(request.POST)
        form = UserCreationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')

    return render(request, 'signup.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('index')



















