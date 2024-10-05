from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.forms import inlineformset_factory

from .models import *
from .forms import *
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
    question = get_object_or_404(Question, id=q_id)

    return render(request, 'poll_result.html', {'question': question})


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




def create_poll(request):
    question_form = QuestionForm()
    choice_formset = ChoiceFormSet()
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        choice_formset = ChoiceFormSet(request.POST)
        if question_form.is_valid() and choice_formset.is_valid():
            question = question_form.save(commit=False)
            question.author = request.user
            question.save()
            choices = choice_formset.save(commit=False)
            for choice in choices:
                choice.question = question
                choice.save()
            return redirect('index')

    return render(request, 'create_poll.html', {
        'question_form': question_form,
        'choice_formset': choice_formset,
    })

def update_poll(request, id):
    question = get_object_or_404(Question, id=id)
    question_form = QuestionForm(instance=question)
    choice_formset = ChoiceFormSet(instance=question)
    if request.method == 'POST':
        question_form = QuestionForm(request.POST, instance=question)
        choice_formset = ChoiceFormSet(request.POST, instance=question)
        if question_form.is_valid() and choice_formset.is_valid():
            question = question_form.save(commit=False)
            question.save()
            choices = choice_formset.save(commit=False)
            for choice in choices:
                choice.question = question
                choice.save()
            return redirect('index')

    return render(request, 'create_poll.html', {
        'question_form': question_form,
        'choice_formset': choice_formset,
    })



def delete_poll(request, id):
    question = get_object_or_404(Question, pk=id)
    question.delete()
    return redirect('index')
