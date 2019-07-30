
from django.contrib import admin
from django.urls import path
from Todo.apps.User import views

urlpatterns = [

    path('signup/', views.SignupView.as_view()),
    path('login/', views.LoginView.as_view()),

]