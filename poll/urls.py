from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('poll/<slug:slug>', views.poll_detail, name='poll_detail'),
    path('poll/results/<slug:slug>', views.poll_results, name='poll_results'),

    path('poll/category/<slug:slug>', views.poll_category, name='poll_category'),
]

