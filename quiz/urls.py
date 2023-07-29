from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index,name='quiz-index'),
    path('register/',views.register,name='register'),
    path('login/',views.customlogin,name='login'),
    path('logout/',views.customlogout,name='logout'),
    path('quizlogs/',views.quizlog,name='quizlogs'),
    path('sections/<str:exam>',views.selectsections,name='sections'),
    path('questions/<str:exam>/<str:section>/',views.questions,name='questions'),
]