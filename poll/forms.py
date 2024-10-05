from django import forms
from django.forms import inlineformset_factory
from .models import *

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('q_text', 'category')

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('c_text',)

ChoiceFormSet = inlineformset_factory(Question, Choice, form=ChoiceForm, extra=4, can_delete=False, max_num=4, min_num=4)
