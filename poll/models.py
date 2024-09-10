from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('poll_category', kwargs={'slug': self.slug})


class Question(models.Model):
    q_text = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.q_text[:50]


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    c_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.c_text[:50]
