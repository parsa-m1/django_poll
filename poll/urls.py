from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('poll/<int:id>', views.poll_detail, name='poll_detail'),
    path('poll/results/<int:q_id>', views.poll_results, name='poll_results'),

    path('poll/category/<slug:slug>', views.poll_category, name='poll_category'),


    path('singup/', views.signup_page, name='singup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),

    path('create/', views.create_poll, name='create_poll'),
    path('update/<int:id>', views.update_poll, name='update_poll'),
    path('delete/<int:id>', views.delete_poll, name='delete_poll'),

]
