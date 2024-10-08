from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('poll_category', kwargs={'slug': self.slug})


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    q_text = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    participants = models.ManyToManyField(User, blank=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.q_text[:50]

    def get_absolute_url(self):
        return reverse('poll_detail', kwargs={'id': self.id})

    def is_voted(self, user):
        if user in self.participants.all():
            return True
        return False

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    c_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.c_text[:50]
